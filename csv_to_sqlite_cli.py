#! /usr/bin/env python3

from attribute_table import build_attributes, build_key_string
from load_csv import load_csv_main
from database_calls import create_database, load_data_into_table
from shared_utilities import read_csv

db_name = input('Name for database >> ')
table_name = input('Name for table >> ')
filename = input('Data file to load >> ')

data, column_names = load_csv_main(filename)

attributes = build_attributes(column_names)

primary_key = build_key_string(table_name, column_names)

create_database(db_name, table_name, attributes, primary_key)

load_data_into_table(db_name, table_name, data)
