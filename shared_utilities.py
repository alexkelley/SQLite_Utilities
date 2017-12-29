#! /usr/bin/env python3

import csv
import os
import itertools
import datetime
import re
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



def clean_data_value(field_value):
    '''
    Parameters:
    - string field value

    Returns
    '''
    data = ''

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

    build_column_data(data_dict)
