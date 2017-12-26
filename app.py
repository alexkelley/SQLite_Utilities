from pprint import pprint as pp

from flask import Flask, render_template, request

from attribute_table import build_attributes, build_key_string
from load_csv import load_csv_main
from database_calls import create_database, load_data_into_table


app = Flask(__name__)


with open('app.secrets', 'r') as f:
    secret_key = f.read().strip()

app.config['SECRET_KEY'] = secret_key


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    data = ''
    if request.method == 'POST':
        filename = form
        data = ['success', filename]
    return render_template("base.html", data=data)


if __name__ == "__main__":
    app.run()
