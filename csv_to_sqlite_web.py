import os

from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Required

from flask_script import Manager
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

from forms import UploadForm, ColumnLabelForm

from shared_utilities import read_csv, clean_column_name, build_column_data
from attribute_table import build_attributes, build_key_string
from database_calls import create_database, load_data_into_table


app = Flask(__name__)

with open('app.secrets', 'r') as f:
    secret_key = f.read().strip()

app.config['SECRET_KEY'] = secret_key

manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
        else:
            raw_data = form.csv_file.data
            filename = secure_filename(raw_data.filename)
            raw_data.save(os.path.join(
                app.instance_path,
                'csv_files',
                filename
            ))
            
            session['csv_filename'] = filename
            
            return redirect(url_for('column_names'))
            
    return render_template('index.html', form=form)


@app.route('/column_names', methods=['GET', 'POST'])
def column_names():
    ## https://stackoverflow.com/questions/22203159/generate-a-dynamic-form-using-flask-wtf-and-sqlalchemy
    ## http://wtforms.readthedocs.io/en/latest/specific_problems.html

    filename = os.path.join(
        app.instance_path,
        'csv_files',
        session['csv_filename']
    )
    
    csv_data = read_csv(filename)

    column_names = []
    for i in csv_data[0]:
        column_names.append(clean_column_name(i))

    class DynamicForm(FlaskForm):
        pass

    for i, name in enumerate(column_names):
        setattr(DynamicForm, '{0}_{1}_col'.format(i, name), StringField('Field {} label:'.format(i+1), default=name))
        setattr(DynamicForm, '{0}_{1}_dt'.format(i, name),
                SelectField('{} data type:'.format(name),
                            choices=[('TEXT', 'TEXT'),
                                     ('INTEGER', 'INTEGER'),
                                     ('REAL', 'REAL'),
                                     ('NULL', 'NULL'),
                                     ('BLOB', 'BLOB')]))

    DynamicForm.submit = SubmitField()

    form = DynamicForm()

    # need to pass some field formatting instructions to the template

    if request.method == 'POST':
        if form.validate() == False:
            flash('Form did not validate.')
        else:
            # retrieve updated column names and values for db_name & table_name
            data_dict = {}
            for field in form:
                data_dict[field.name] = field.data

            session['column_data'] = data_dict
                        
            return redirect(url_for('primary_key'))
        
    return render_template('column_names.html', form=form)


@app.route('/primary_key')
def primary_key():

    if session['column_data']:
        column_data = session['column_data']
    else:
        column_data = 'No data returned'

    attribute_table = build_column_data(column_data)
    
    return render_template('primary_key.html', column_data=attribute_table)


if __name__ == "__main__":
    manager.run()
