#! /usr/bin/env python3

import csv
import os


def prompt_for_filename():
    '''
    Returns a string of the filename
    '''
    pass


def check_file_size(filename):
    '''
    Takes a string filename

    Returns a float of the size of the file
    '''
    pass


def user_prompt_column_labels():
    '''
    Find out from user if first row contains column names
    Provide an option to edit or create column labels

    Returns a list of column names
    '''
    pass

    
def read_csv(filename, column_names):
    '''
    Parameters:
        - string filename
        - list of column names

    Returns a list of dictionaries mapping column names to field values 
    '''
    data_list = []
    temp_dict = {}
    
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        # parse & display to user the first row to determine if they are column labels
        # user_prompt_column_labels()
        for row in reader:
            pass

    return data_list


##################
# Function Calls #
##################

def main():
    # ask user for filename
    # check if filesize is acceptable
    # build list of column labels
    # read in csv and return list of dictionaries {'col_name1': 'field_value', 'col_name2': 'field_value',}


if __name__ == '__main__':
    main()
