#! /usr/bin/env python3

from attribute_table import build_attributes
from generate_insert_statement import generate_insert
from load_csv import load_csv_main
from create_database import 

data, column_names = load_csv_main()

attributes = build_attributes(column_names)

# need to add a primary key here

db_name = 'test.db'
table_name = 'customers-test'

create_database(db_name, table_name, attribute_dict, primary_key)

for i in data:
    print(generate_insert(table_name, i))

