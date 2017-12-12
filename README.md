# SQLite Utilities

A collection of general purpose Python utilities for working with SQLite databases

## Done - create_database.py
## Done - load_table.py
## Done - generate_insert_statement.py
Format the SQL INSERT statement for use in the load_table.py script
## IN PROGRESS - [load_csv.py](https://github.com/alexkelley/SQLite_Utilities/blob/master/load_csv.py)
read csv file and map column names to each field value in a dictionary.

Display the first line to the user at a command prompt.  Ask if these are the column names to use.
If yes, build a list of those names in the order listed.  If no, prompt the user to enter an alternative name, column by column (This could merely rename the columns).

Next ask user if the first line was data to include in the data structure (dictionary) to be built.  If yes, start at first line.  If no, start at next line.  Build a json-style dictionary for each row with the key as the column name (from the list) and the value from the next parsed row field.
## TODO - build_attributes.py
With user prompt, take a list of column labels and select its data type from a list of approved types.  Zipper this together into a json-style dictionary.  At the end, ask user to define a primary key and any foreign keys.
## TODO - build the primary key / foreign key string
