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


def build_key_string(table_name, column_names):
    '''
    Parameters:
        - string table name

    Returns:
        - dictionary of {'key': key_string}
    '''
    key_string = 'CONSTRAINT '
    
    key_string_dict = {'key': key_string}

    for i, name in enumerate(column_names):
        print('{0}. {1}'.format(i+1, name))

    keys = input('Fields to be the table primary key(s) (separate with comma) >> ')

    keys = keys.split()

    pk_name = input('Enter a name for your primary key >> ')

    key_string += '{0}\nPRIMARY KEY '.format(pk_name)

    ## call function to build foreign key with a while loop 
    
    '''
    CONSTRAINT transaction_pk
        PRIMARY KEY (transaction_id, company_id),

    CONSTRAINT transactions_fk
        FOREIGN KEY (company_id)
            REFERENCES company(company_id)
    '''

    return key_string_dict

##################
# Function Calls #
##################

if __name__ == '__main__':
    # Test data
    column_names = ['cid', 'company', 'licenses', 'dollars']
    pprint.pprint(build_attributes(column_names))
