#! /usr/bin/env python3

import csv
import os
import itertools
import datetime
import re
import sqlite3
import sys
from pprint import pprint as pp


def read_csv(filename):
    '''
    Parameters:
        - string filename

    Returns a list of lists populated by csv file data
    '''
    data_list = []
    temp_list = []
    
    with open(filename, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            for i in row:
                # place to add data validation and cleaning
                temp_list.append(i)
            data_list.append(temp_list)
            temp_list = []

    return data_list

    
def clean_column_name(field_value):
    '''
    Parameters:
    - string field value

    Returns
    '''
    if field_value is None:
        field_value = 'NULL'
        
    data = ''
    
    if field_value != 'NULL' and isinstance(field_value, str):
        data1 = field_value.lower().strip().replace(' ', '_')
    
        data = data1.replace('#', 'num').replace('%', 'percent').replace('$', '').replace('"', '').replace("'", "").replace(',', '')
        
    elif isinstance(field_value, datetime.date):
        data = datetime.datetime.strftime(field_value, '%Y-%m-%dT%H-%M-%S')

    else:
        data = field_value


    return data


def build_column_data(data_dict):
    '''
    Parameters:
    - dictionary of data returned from web form

    Returns
    - Attribute dictionary
    '''    
    attributes = {}

    all_keys = data_dict.keys()
  
    col_keys = []

    # match from the start of string, 1 or more digits then an underscore
    pattern = re.compile(r"^\d+_")
    
    for i in all_keys:
        result = pattern.match(str(i))
        if result:
            col_keys.append(i)

    # group column names with respective data type
    temp_dict = {}
    for i in col_keys:
        num = i.split('_')[0]
        if num in temp_dict:
            temp_dict[num].append(i)
        else:
            temp_dict[num] = [i]

    # build attribute table from column groups
    count = 0
    for field in temp_dict.values():
        for value in field:
            if '_col' in value:
                name = data_dict[value]
            elif '_dt' in value:
                data_type = data_dict[value]
    
        attributes[count] = {'name': name, 'data_type': data_type}
        count += 1

    column_list = []
    for value in attributes.values():
        column_list.append(value['name'])

    return (column_list, attributes)


def build_key_string(table_name, column_names):
    '''
    Parameters:
        - list of column names to use in primary key

    Returns:
        - string specifying primary key and any foreign keys
    '''
    temp_key_string = ', '.join(column_names)

    primary_key_name = table_name + '_pk'

    key_string = 'CONSTRAINT {0} PRIMARY KEY ({1})'.format(
        primary_key_name, temp_key_string)

    return key_string


def create_database(db_name, table_name, attribute_dict, primary_key):
    '''
    Parameters:
        1. string database name
        2. string table name
        3. dictionary of table attributes
            'table': {
                0: {'column_name': 'ID', 'data_type': 'INTEGER'},
                1: {'column_name': 'backend', 'data_type': 'TEXT'},
                ...
            }

        4. string for primary key
           primary_key = 
              'CONSTRAINT transaction_pk
                   PRIMARY KEY (transaction_id, company_id),

               CONSTRAINT transactions_fk
                   FOREIGN KEY (company_id)
                       REFERENCES company(company_id)'

    Returns:
        - True if successful
        - False if not successful
    '''
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS {}'.format(table_name))
    
    build_table_sql = 'CREATE TABLE {} (\n'.format(table_name)


    for key, value in attribute_dict.items():
        build_table_sql += "\t{} {},\n".format(value['name'], value['data_type'])

    build_table_sql += '\n\t{}\n);'.format(primary_key)
    
    try:
        cursor.execute(build_table_sql)
        flag = True
        print('{} database created.'.format(db_name))

    except:
        print(sys.exc_info())
        print(build_table_sql)
        flag = False

    finally:
        conn.commit()
        cursor.close()
        conn.close()

    return flag


def clean_data_value(field_value):
    '''
    Parameters:
    - string field value

    Returns
    '''
    data = ''

    return data


def map_column_name_to_data_value(column_names, csv_data):
    '''
    Parameters:
        - list of column names
        - list of lists containing csv data

    Returns a list of dictionaries mapping column names to field values 
    '''
    data_list = []
    temp_dict = {}
    for row in csv_data:
        for i in range(len(column_names)):
            temp_dict[column_names[i]] = row[i]
        data_list.append(temp_dict)
        temp_dict = {}

    return data_list

            
def generate_insert(table_name, field_value_dict):
    '''
    Parameters:
        1. string table_name
        2. dictionary of values in the form:
           {column_name1: field_value, 
            column_name2: field_value,
            ...}
    
    Returns:
        - string SQLite3 INSERT statement
    '''
    value_string = ''
    column_string = ''

    for label, value in field_value_dict.items():
        if value is None:
            value = 'NULL'

        if value != 'NULL' and isinstance(value, str):
            value_string += "'{}', ".format(value.replace("'", "").replace("%", "").replace("$", "").replace(",", ""))
        elif isinstance(value, datetime.date):
            value_string += "'{}', ".format(value)
        else:
            value_string += "{}, ".format(value)

        column_string += "{}, ".format(label.replace("'", ""))

        sql_string = "INSERT INTO {0} ({1}) VALUES ({2});".format(
            table_name, column_string[:-2], value_string[:-2])

    return sql_string


def load_data_into_table(db_name, table_name, data_list):
    '''
    
    '''
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()    

    for record in data_list:
        sql_call = generate_insert(table_name, record)

        try:
            cursor.execute(sql_call)
        except:
            print(sys.exc_info())
            print(sql_call)
            break

    conn.commit()
    cursor.close()
    conn.close()


#################
# Testing Calls #
#################

if __name__ == "__main__":

    row = ['Job #',
           'Type',
           "Invoice's Date",
           '"Customer"',
           'Job Total',
           'Commission,$',
           'Commission %'
    ]

    data_dict = {'1_fun_col': 'column1',
                 '0_good_col': 'column0',
                 '23_excellent_col': 'column2',
                 '1_fun_dt': 'TEXT',
                 '0_good_dt': 'INTEGER',
                 '23_excellent_dt': 'REAL',
                 'db_name': 'test.db',
                 'csrf_token': 'sjfosahgoihngio'
    }
    # for i in row:
    #     print(clean_column_name(i))

    # build_column_data(data_dict)

    # table_name = 'JobCost'
    # column_names = ['job_num', 'company_name']
    # print(build_key_string(table_name, column_names))
