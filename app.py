import os

from flask import Flask, render_template, request, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap

from forms import UploadForm

from attribute_table import build_attributes, build_key_string
from load_csv import load_csv_main
from database_calls import create_database, load_data_into_table


app = Flask(__name__)

with open('app.secrets', 'r') as f:
    secret_key = f.read().strip()

app.config['SECRET_KEY'] = secret_key

manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    csv_file = None
    data = None
    form = UploadForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
        else:
            data = form.csv_file.data
            flash('Success!')
            
    return render_template('index.html', form=form, data=data)


if __name__ == "__main__":
    manager.run()
