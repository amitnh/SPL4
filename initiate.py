from Persistence_Layer import *

def main():
    repo.create_tables()
    print("Hello World")
    repo.employees.insert(Employee(12, "tal", 15, 2))
    repo.suppliers.insert(Supplier(1,"asd","1800400400-asd"))
    repo.products.insert(Product(123,"magnus",156,1))
    repo.coffee_stands.insert(Coffee_stand(2,"BLD2",2))

    repo.activities.insert(Activity(123,50,1,"10012020"))
    repo.activities.insert(Activity(123,50,1,"10012020"))
    repo.activities.insert(Activity(123,50,1,"10012020"))

    tal = repo.employees.find(12)
    print(tal.name)
    asd = repo.suppliers.find(1)
    print(asd.contact_information)
    print(repo.activities.findall())


main()


