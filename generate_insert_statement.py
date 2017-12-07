#! /usr/bin/env python3

def generate_insert(table_name, field_value_dict):
    '''
    Takes:
        1. string table_name
        2. dictionary of values {column_name: field_value}
    
    Returns:
        - string SQLite3 INSERT statement
    '''
    value_string = ''
    column_string = ''

    for label, value in field_value_dict.items():
        if value is None:
            value = 'NULL'

        if value != 'NULL' and isinstance(value, str):
            value_string += "'{}', ".format(value.replace("'", ""))
        elif isinstance(value, datetime.date):
            value_string += "'{}', ".format(value)
        else:
            value_string += "{}, ".format(value)

        column_string += "{}, ".format(label.replace("'", ""))

        sql_string = "INSERT INTO {0} ({1}) VALUES ({2});".format(
            table_name, column_string[:-2], value_string[:-2])

    return sql_string
