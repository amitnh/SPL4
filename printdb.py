import sqlite3

from Persistence_Layer import *


def print_table(table):
    _conn = repo.return_conn()
    cursor = _conn.cursor()
    if table == "activities":
        cursor.execute('SELECT * FROM ' + table + ' ORDER BY date')
    else:
        cursor.execute('SELECT * FROM ' + table + ' ORDER BY id')

    list1 = cursor.fetchall()
    print(format(table).capitalize())
    for item in list1:
        print(item)


print_table("activities")
print_table("coffee_stands")
print_table("employees")
print_table("products")
print_table("suppliers")

print()
print("Employees report")
repo.employees_report()

print()
print("Activities")
lines = repo.activities_report()
if lines!=[]:
    for line in lines:
        print(line)