import os

from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import Required

from flask_script import Manager
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

from forms import UploadForm

from shared_utilities import *


app = Flask(__name__)

with open('app.secrets', 'r') as f:
    secret_key = f.read().strip()

app.config['SECRET_KEY'] = secret_key

manager = Manager(app)
bootstrap = Bootstrap(app)

##################
# View Functions #
##################

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
        else:
            # retrive form data and save file to web server
            form_data = form.csv_file.data
            csv_filename = secure_filename(form_data.filename)
            csv_path_filename = os.path.join(app.instance_path,
                                             'csv_files',
                                             csv_filename
            )
            form_data.save(csv_path_filename)

            # set session variable for absolute path to csv file
            session['csv_filename'] = csv_path_filename
            
            return redirect(url_for('column_names'))
            
    return render_template('index.html', form=form)


@app.route('/column_names', methods=['GET', 'POST'])
def column_names():
    ## https://stackoverflow.com/questions/22203159/generate-a-dynamic-form-using-flask-wtf-and-sqlalchemy
    ## http://wtforms.readthedocs.io/en/latest/specific_problems.html

    csv_data = read_csv(session['csv_filename'])

    column_names = []
    for i in csv_data[0]:
        column_names.append(clean_column_name(i))

    # create a form dynamically from first row of csv data
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

    if request.method == 'POST':
        if form.validate() == False:
            flash('Form did not validate.')
        else:
            # retrieve updated column names and data types
            data_dict = {}
            for field in form:
                data_dict[field.name] = field.data

            session['column_data'] = data_dict
                        
            return redirect(url_for('primary_key'))
        
    return render_template('column_names.html', form=form)


@app.route('/primary_key', methods=['GET', 'POST'])
def primary_key():

    if session['column_data']:
        column_data = session['column_data']
    else:
        column_data = 'No data returned'

    column_names, table_attributes = build_column_data(column_data)

    session['table_attributes'] = table_attributes
    
    class DynamicForm(FlaskForm):
        pass

    # build field list for multi-select box in form
    key_choices = []
    for name in column_names:
        key_choices.append((name, name))
        
    setattr(DynamicForm,
            'primary_keys',
            SelectMultipleField(
                'Use Ctrl to select more than one field for the primary key:',
                choices=key_choices)
    )
    
    DynamicForm.db_name = StringField(
        'Enter a database name:', validators=[Required()])
    DynamicForm.table_name = StringField(
        'Enter a table name:', validators=[Required()])
    DynamicForm.submit = SubmitField()
    
    form = DynamicForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('Form did not validate.')
        else:
            data_dict = {}
            for field in form:
                data_dict[field.name] = field.data

            session['db_setup_data'] = data_dict
                        
            return redirect(url_for('confirmation'))
    
    return render_template('primary_key.html', form=form, column_data=table_attributes)


@app.route('/confirmation')
def confirmation():

    if session['db_setup_data']:
        data = session['db_setup_data'] 
    else:
        data = 'Failure'
        
    db_name = os.path.join(app.instance_path,
                           'databases',
                           session['db_setup_data']['db_name']
            )
    table_name = session['db_setup_data']['table_name']
    attributes = session['table_attributes']
    
    key_columns = session['db_setup_data']['primary_keys']
    primary_key_string = build_key_string(table_name, key_columns)

    create_database(db_name, table_name, attributes, primary_key_string)
    
    return render_template('confirmation.html', data=data)
    
if __name__ == "__main__":
    manager.run()
