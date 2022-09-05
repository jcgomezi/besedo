
import enum
import sqlite3
import pandas as pd
import os
from besedo.settings import BASE_DIR
DB_NAME = os.path.join(BASE_DIR, "db.sqlite3")
print("database to use: \n"+DB_NAME)

def get_database_connection():
    con = sqlite3.connect(DB_NAME)
    return con

def create_table(query,**kwargs):
    con = get_database_connection()
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def update_register(table,**kwargs):
    con = get_database_connection()
    query = f'''UPDATE {table}
            SET '''
    for index,key in enumerate(kwargs):
        if index != 0:
            query += f" {key} = '{kwargs[key]}', "
    query = query[:-2] + f''' where id = {kwargs['id']}'''
    print(query)
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()



def delete_register(table,**kwargs):
    con = get_database_connection()
    query = f'''DELETE FROM {table}
            WHERE id = '{kwargs['id']}' '''
    print(query)
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()



def insert_new_value_into_table(table,**kwargs):
    con = get_database_connection()
    query = f'''SELECT * FROM {table}'''
    df = get_db_data_into_df(query)
    xid = df.iloc[-1,0] + 1 if len(df)>0 else 1
    query = f'''
    INSERT INTO {table}
    VALUES({xid}
    '''
    for index,key in enumerate(kwargs):
        print(key)
        query += f",'{kwargs[key]}' "        
    query += ')'
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def get_db_data_into_df(query):
    con = get_database_connection()
    cursor = con.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    colnames = cursor.description
    columns = []
    try:
        for row in colnames:
            columns.append(row[0])
        df.columns = columns
    except:
        print("no columns can be fetched")
    cursor.close()
    return df


def clean_db_table(table):
    con = get_database_connection()
    cursor = con.cursor()
    cursor.execute(f'DELETE FROM {table}')
    con.commit()
    cursor.close()
    con.close()

# query = f'''CREATE TABLE contacts (
# 	id INTEGER PRIMARY KEY,
# 	first_name TEXT NOT NULL,
# 	last_name TEXT NOT NULL,
# 	email TEXT NOT NULL UNIQUE,
# 	phone TEXT NOT NULL UNIQUE,
#     age INTEGER
#     );'''

# create_table(con,query)