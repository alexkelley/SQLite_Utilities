#! /usr/bin/env python3

import csv
import os


def prompt_for_filename():
    '''
    Returns a string of the filename
    '''
    filename = input("Data file to load >> ")

    return filename


def get_file_size(filename):
    '''
    Takes a string filename

    Returns a float of the size of the file
    '''
    if os.path.isfile(filename):
        file_info = os.stat(filename)
        return file_info.st_size

    else:
        return 0


def user_prompt_column_labels(first_row):
    '''
    Find out from user if first row contains column names
    Provide an option to edit or create column labels

    Returns a list of column names
    '''

    print(first_row)
    flag = input('Does the first row contain column labels (Y/N)? >> ')

    if flag == 'Y':
        flag = True
    else:
        flag = False
        
    column_labels = []
    for i, label in enumerate(first_row):
        print('{0}: {1}'.format(i, label))
        new_label = input('New label for {} (blank leaves label unchanged) >> '.format(i))

        if new_label:
            column_labels.append(new_label)
        else:
            column_labels.append(label)

    return (column_labels, flag)

    
def read_csv(filename):
    '''
    Parameters:
        - string filename
        - list of column names

    Returns a list of dictionaries mapping column names to field values 
    '''
    data_list = []
    temp_dict = {}
    
    with open(filename, 'r') as f:
        reader = csv.reader(f)

        first_row = next(reader)

        column_names, flag = user_prompt_column_labels(first_row)
        print(column_names)

        if not flag:
            reader.seek(0)

        for row in reader:
            data_list.append(row)

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

    data = read_csv(filename)

    #print(data[:2])
    
    # build list of column labels
    # return list of dictionaries {'col_name1': 'field_value', 'col_name2': 'field_value',}


if __name__ == '__main__':
    main()
