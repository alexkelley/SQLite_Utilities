#! /usr/bin/env python3
import sqlite3

def load_data(db_name, table_name, listofdicts):
    '''
    Parameters:
        1. string database name
        2. string table name
        3. list of dictionaries 
           {column_name1: field_value, column_name2: field_value, ...}

    Returns:
        - True if successful
        - False if not successful
    '''
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()    

    for record in listofdicts:
        sql_call = generate_insert(table_name, record)

        try:
            cursor.execute(sql_call)
        except:
            print(sys.exc_info())
            print(sql_call)
            return False

    conn.commit()
    cursor.close()
    conn.close()

    return True
