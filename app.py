import os

from flask import Flask, render_template, request
from flask_script import Manager
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
#from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired

from attribute_table import build_attributes, build_key_string
from load_csv import load_csv_main
from database_calls import create_database, load_data_into_table


app = Flask(__name__)

with open('app.secrets', 'r') as f:
    secret_key = f.read().strip()

app.config['SECRET_KEY'] = secret_key

manager = Manager(app)
bootstrap = Bootstrap(app)

class UploadForm(FlaskForm):
    #csv_file = FileField('Select a file to upload >> ', validators=[FileRequired()])
    csv_file = StringField('Enter some data:', validators=[DataRequired()])
    
@app.route('/', methods=['GET', 'POST'])
def index():
    csv_file = None
    data = None
    form = UploadForm()
    if form.validate_on_submit():
        f = form.csv_file.data
        data = f.filename

    return render_template('index.html', form=form, data=data)


if __name__ == "__main__":
    manager.run()
