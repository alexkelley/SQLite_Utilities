from pprint import pprint as pp

from flask import Flask, render_template, request

# import main logic from other files
#from weather import get_local_time, query_api

app = Flask(__name__)


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    data = []
    error = None
    if request.method == 'POST':
        data.append('success')
    return render_template("main.html",
                           data=data,
                           error=error)


if __name__ == "__main__":
    app.run()
