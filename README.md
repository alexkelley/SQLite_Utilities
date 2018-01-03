# SQLite Utilities

csv_to_sqlite_web.py is a Flask web application to:
* upload a csv file
* create column labels
* assign data types to each attribute
* create a SQLite database.


## Installation

`git clone https://github.com/alexkelley/sqlite-utilities.git

Create a virtual environment for Python3

From the main file directory,
` pip install requirements.txt

Run the program
` python csv_to_sqlite_web.py runserver

Then navigate in a web brower to http://127.0.0.1:5000/ 

## Future

* re-implement csv_to_sqlite_cli.py, command line interface version
* error handling
* tests
* support for more databases
* support for more input file types
