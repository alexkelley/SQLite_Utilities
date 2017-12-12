#! /usr/bin/env python3

import csv
import os


def prompt_for_filename():
    '''
    Returns a string of the filename
    '''
    filename = input("Data file to load (enclose in quotes) >> ")

    return filename


def get_file_size(filename):
    '''
    Takes a string filename

    Returns a float of the size of the file
    '''
    if os.path.isfile(filename):
        file_info = os.stat(filename)

    return file_info.st_size


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
    filename = prompt_for_filename()
    # check if filesize is acceptable
    if get_file_size(filename) < 1000000000:
        print('\nfile:{} is not too big.\n'.format(filename))
    # build list of column labels
    # read in csv and return list of dictionaries {'col_name1': 'field_value', 'col_name2': 'field_value',}


if __name__ == '__main__':
    main()
