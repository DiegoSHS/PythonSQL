import pymysql
from pymysql import Error,Connection

def connex(options):
    try:
        conection = pymysql.connect(**options)
        return conection
    except pymysql.Error as err:
        print(err)
        return

def selectAll(conection:Connection,table:str):
    cursor = conection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    return rows

def close(cursor):
    cursor.commit()
    cursor.close()