#! /usr/bin/env python3
import sqlite3

def load_data(db_name, table_name, list_of_dicts):
    '''
    Parameters:
        1. string database name
        2. string table name
        3. list of dictionaries containing column names mapped to field values
           {column_name1: field_value, column_name2: field_value, ...}

    Returns:
        - True if successful
        - False if not successful
    '''
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()    

    for record in list_of_dicts:
        sql_call = generate_insert(table_name, record)

        try:
            cursor.execute(sql_call)
            flag = True

        except:
            print(sys.exc_info())
            print(sql_call)
            flag = False

        finally:
            conn.commit()
            cursor.close()
            conn.close()

    return flag
