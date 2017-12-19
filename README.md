# SQLite Utilities

A collection of general purpose Python utilities for working with SQLite databases
---
The user selects a csv file via command line (web interface coming) and parses the first line of data to determine if it contains labels or not.  The user can edit the labels or create new labels if none exist.  The program automatically removes whitespace, special characters and capitalized letters (need to add support for converting camelCase to camel_case) from existing column labels.  Finally, the data is loaded into a SQLite database (need to add support for user interface in taking db and table names).  

Future tasks:
## Done - [database_calls.py](https://github.com/alexkelley/SQLite_Utilities/blob/master/database_calls.py)
## Done - [load_table.py](https://github.com/alexkelley/SQLite_Utilities/blob/master/load_table.py)
## Done - [generate_insert_statement.py](https://github.com/alexkelley/SQLite_Utilities/blob/master/generate_insert_statement.py)
Format the SQL INSERT statement for use in the load_table.py script
## DONE v1 - [load_csv.py](https://github.com/alexkelley/SQLite_Utilities/blob/master/load_csv.py)
### TODO - build support for different file types

## DONE - build_attributes.py
With user prompt, take a list of column labels and select its data type from a list of approved types.  Zipper this together into a json-style dictionary.  At the end, ask user to define a primary key and any foreign keys.
## DONE - build_key.py
build the primary key / foreign key string
## TODO - web ui
Flask webserver that spins up upon running the script.  Form takes database and table name.  Column labels populate a table with a column for data type (dropdown select box) with inference made from data source.  Will need to refactor the script in an MVC way to separate the user interface elements so that the main logic can work with both web UI and CLI. 
