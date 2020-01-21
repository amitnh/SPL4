import sys
from Persistence_Layer import *
from printdb import printdb

action = open(sys.argv[1], "r")
toadd = action.read().split('\n')
for line in toadd:
    line = line.split(', ')
    currQua= repo.products.find(line[0]).quantity
    newQ = currQua+int(line[1])
    id =int(line[0])
    if  newQ>0:
        repo.activities.insert(Activity(line[0], line[1], line[2], line[3]))
        repo.products.update(id,newQ)

printdb()
print()
print("Employees report")
cursor = repo._conn.cursor()
cursor.execute("""
SELECT * FROM employees ORDER BY employees.name
""")
employees = cursor.fetchall()
i=0
totalincome =[]
for emp in employees:
    cursor.execute("""
    SELECT a.product_id, a.quantity , p.price
    FROM activities a, products p
    WHERE a.activator_id = ? AND a.product_id = p.id 
    """, [emp[0]])
    lines = cursor.fetchall()
    totalincome.append(0)
    for line in lines:
        totalincome[i]+= line[1] * -line[2]
    print(str(emp[1]) + ", " + str(emp[2])+ ", " +repo.coffee_stands.find(emp[3]).location+ ", " +str(totalincome[i]))
    i += 1

print()
print("Activities")
cursor.execute("""
        SELECT a.date, p.description , p.quantity, e.name, s.name
        FROM activities a 
        JOIN products p ON p.id = a.product_id
        LEFT JOIN  suppliers s ON a.activator_id = s.id
        LEFT JOIN  employees e ON  a.activator_id = e.id
        """)
lines = cursor.fetchall()
totalincome.append(0)
for line in lines:
    print(line)

































