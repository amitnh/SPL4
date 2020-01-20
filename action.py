import sys

from Persistence_Layer import *
def action():
    # action = open(sys.argv[1], "r")
    action = open("action.txt", "r")

    toadd = action.read().split('\n')
    for line in toadd:
        line = line.split(', ')
        repo.activities.insert(Activity(line[0],line[1],line[2],line[3]))
        currQua= repo.products.find(line[0]).quantity
        newQ = currQua+int(line[1])
        id =int(line[0])
        if  newQ>0:
            repo.products.update(id,newQ)

