import pymysql
from pymysql import Connection


def connex(options: dict):
    try:
        connection = pymysql.connect(**options)
        print(connection)
        return connection
    except pymysql.Error as err:
        print(err)
        return


def select_all(connection: Connection, table: str):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table};")
    rows = cursor.fetchall()
    return rows


def close(connection: Connection):
    cursor = connection.cursor()
    cursor.commit()
    cursor.close()


def insert_many(connection: Connection, items_list: list):
    cursor = connection.cursor()
    for item in items_list:
        cursor.intert(**item)


separator = ', '


def insert_one(connection: Connection, table: str, item: dict):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {table} ({separator.join(item.keys())}) values ({separator.join(item.values())})")


command = f"CREATE TABLE products (id INT PRIMARY KEY, name VARCHAR(30), description VARCHAR(200),price DOUBLE)"
conn_options = {"user": 'diego', "host": 'localhost', "password": 'Dla.2002/mysql', "database": "products"}


def main():
    connection = connex(conn_options)
    rows = select_all(connection=connection, table='products')
    print(rows)
    for row in rows:
        print(row)


main()
