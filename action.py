import sys
from Persistence_Layer import *

action = open(sys.argv[1], "r")
toadd = action.read().split('\n')
for line in toadd:
    line = line.split(', ')
    currQua= repo.products.find(line[0]).quantity
    newQ = currQua+int(line[1])
    id =int(line[0])
    if  newQ>=0:
        repo.activities.insert(Activity(line[0], line[1], line[2], line[3]))
        repo.products.update(id,newQ)

import printdb



































