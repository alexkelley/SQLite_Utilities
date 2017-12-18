#! /usr/bin/env python3

from attribute_table import build_attributes, build_key_string
from generate_insert_statement import generate_insert
from load_csv import load_csv_main
from database_calls import create_database, load_data_into_table


data, column_names = load_csv_main()

attributes = build_attributes(column_names)

primary_key = build_key_string(column_names)

db_name = '../test.db'
table_name = 'customers-test'

create_database(db_name, table_name, attributes, primary_key)

#load_data_into_table(db_name, table_name, data_list)
