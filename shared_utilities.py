#! /usr/bin/env python3

import csv
import os
import datetime

    
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





if __name__ == "__main__":

    row = ['Job #',
           'Type',
           "Invoice's Date",
           '"Customer"',
           'Job Total',
           'Commission,$',
           'Commission %'
    ]

    for i in row:
        print(clean_column_name(i))
