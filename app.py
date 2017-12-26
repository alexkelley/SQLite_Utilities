from pprint import pprint as pp

from flask import Flask, render_template, request

from attribute_table import build_attributes, build_key_string
from load_csv import load_csv_main
from database_calls import create_database, load_data_into_table


app = Flask(__name__)


@app.route('/')
@app.route('/', methods=['POST'])
def index():

    # get filename from webform
    
    data, column_names = load_csv_main(filename)

    # display csv data in tabular format
    # ui for specifying db_name, table_name and column_names
    error = None
    if request.method == 'POST':
        data.append('success')
    return render_template("main.html",
                           data=data,
                           error=error)


if __name__ == "__main__":
    app.run()
