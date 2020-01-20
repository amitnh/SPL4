import sys

from Persistence_Layer import *
from printdb import printdb

repo.create_tables()
_conn = sqlite3.connect('moncafe.db')

config1 = open(sys.argv[1], "r")
toadd = config1.read().split('\n')
for line in toadd:
    line = line.split(', ')
    if line[0] == 'C':
        repo.coffee_stands.insert(Coffee_stand(line[1], line[2], line[3]))
    elif line[0] == 'S':
        repo.suppliers.insert(Supplier(line[1], line[2], line[3]))
    elif line[0] == 'E':
        repo.employees.insert(Employee(line[1], line[2], line[3], line[4]))
    elif line[0] == 'P':
        repo.products.insert(Product(line[1], line[2], line[3], 0))
_conn.commit()
_conn.close()

printdb()




