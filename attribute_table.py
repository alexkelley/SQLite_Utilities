#! /usr/bin/env python3

import pprint
import time


def get_data_type():
    '''
    Prompts user to select an approved SQLite data type.
    
    Parameters: dictionary of data types for use with SQLite
    
    Returns: string name of the data type selected
    '''
    data_types = {1: 'TEXT', 2: 'INTEGER', 3: 'REAL', 4: 'NULL', 5: 'BLOB'}
    
    for key, label in sorted(data_types.items()):
        print('{0}. {1}'.format(key, label))

    selection = input('Select number for data type: ')

    return data_types[int(selection)]


def build_attributes(column_names):
    attributes = {}
    
    for i, name in enumerate(column_names):
        print('\n{}'.format(name))
        data_type = get_data_type()
        attributes[i] = {'name': name, 'data_type': data_type}

    return attributes


def add_foreign_key():
    '''
    
    '''
    fk_string = ''
    fk_field = input('Field to be foreign key >> ')
    fk_name = input('Name for foreign key >> ')
    fk_ref_table = input('Reference table >> ')
    fk_ref_field = input('Reference field >> ')

    fk_string += 'CONSTRAINT {0} FOREIGN KEY ({1}) REFERENCES {2}({3})'.format(fk_name, fk_field, fk_ref_table, fk_ref_field)

    return fk_string


def build_key_string(column_names):
    '''
    Parameters:
        - list of column names

    Returns:
        - string specifying primary key and any foreign keys
    '''
    key_string = 'CONSTRAINT '

    for i, name in enumerate(column_names):
        print('{0}. {1}'.format(i, name))

    primary_keys = input('Fields to be the table primary key(s) (separate with comma) >> ')

    primary_keys = primary_keys.split()

    temp_key_string = ''
    for i in primary_keys:
        temp_key_string += '{}, '.format(column_names[int(i)])

    pk_name = input('Enter a name for your primary key >> ')

    key_string += '{0} PRIMARY KEY ({1})'.format(pk_name, temp_key_string[:-2])

    fk_flag = input('Add a foreign key? (Y or N) >> ')

    while fk_flag == 'Y':
        key_string += ', {}'.format(add_foreign_key())

        fk_flag = input('Add another foreign key? (Y or N) >> ')

    return key_string



##################
# Function Calls #
##################

if __name__ == '__main__':
    # Test data
    column_names = ['cid', 'company', 'licenses', 'dollars']
    # pprint.pprint(build_attributes(column_names))
    pprint.pprint(build_key_string(column_names))
