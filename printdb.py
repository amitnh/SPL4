import sqlite3


def print_table(table):
    _conn = sqlite3.connect('moncafe.db')
    cursor = _conn.cursor()
    cursor.execute('SELECT * FROM ' + table )

    list = cursor.fetchall()
    print(format(table) + ':')
    for item in list:
        print(item)

    cursor.close()


def printdb():
    # _conn = sqlite3.connect('moncafe.db')
    # cursor = _conn.cursor()
    print_table("suppliers")
    print_table("employees")
    print_table("products")
    print_table("coffee_stands")
