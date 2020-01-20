import sqlite3

from Persistence_Layer import *


def print_table(table):
    _conn = repo.return_conn()
    cursor = _conn.cursor()
    cursor.execute('SELECT * FROM ' + table)
    list1 = cursor.fetchall()
    print(format(table) + ':')
    for item in list1:
        print(item)


def printdb():
    print_table("suppliers")
    print_table("employees")
    print_table("products")
    print_table("coffee_stands")
