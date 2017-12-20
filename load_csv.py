#! /usr/bin/env python3

import csv
import os


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
    print('### First row of data from csv file ###\n\n{}\n'.format(first_row))
    
    flag = input('Does the first row contain column labels (Y/N)? >> ')

    if flag == 'Y':
        flag = True
    else:
        flag = False
        
    column_labels = []
    print('\n### Re-name columns in database ###')
    for i, label in enumerate(first_row):
        label = label.lower().strip()
        replacement_dict = {'#': 'num', ' ': '_', '%': 'percent'}
        for key, value in replacement_dict.items():
            label = label.replace(key, value)
        print('\n{0}: {1}'.format(i, label))
        new_label = input('New label for {} (Enter to leave label unchanged) >> '.format(i))

        if new_label:
            column_labels.append(new_label)
        else:
            column_labels.append(label)

    print('\n### New column labels list created ###\n')

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
            for i in range(len(column_names)):
                temp_dict[column_names[i]] = row[i]
            data_list.append(temp_dict)
            temp_dict = {}

    return (data_list, column_names)


##################
# Function Calls #
##################

def load_csv_main(filename):
    # check if filesize is acceptable
    file_size = get_file_size(filename)
    print('\nfile:{0} is {1} bytes.\n'.format(filename, file_size))

    data, column_names = read_csv(filename)

    return (data, column_names)


if __name__ == '__main__':
    load_csv_main()
