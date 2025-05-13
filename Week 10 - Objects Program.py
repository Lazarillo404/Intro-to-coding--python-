"""
Created on Sun Apr 27 10:35:12 2025

@author: Mateusz
"""
"""
This is a program that represents people that work for a company.
It will create a single class called employee.
The class will have several built in methods to allow you to update and display information about the employee.
"""
# create the class
class employee(): 
    # create constructor that holds employee name, ID, and salary
    def __init__(self, name, idNum, salary):
        self.name = name
        self.set_ID_num(idNum)
        self.set_salary(salary)
        
    def print_emp(self):
        print(f"Employee: {self.name:25} ID: {self.idNum:7} Salary: ${self.salary:10.2f}")

    def increase_salary(self, incrementAmount):
        if incrementAmount <= 0:
            print("Error: the salary cannot be increased")
        else:
            self.salary += incrementAmount

    def set_ID_num(self, newIDnum):
        if newIDnum < 1000 or newIDnum > 9999999:
            print("Error: the new identification number is invalid. It will be set to 1000")
            self.idNum = 1000
        else:
            self.idNum = newIDnum

    def set_salary(self, newSalary):
        if newSalary <= 0:
            print("Error: the passed in salary is invalid. The salary will be set to 0.00")
            self.salary = 0.00
        else:
            self.salary = newSalary

    def get_ID_num(self):
        return self.idNum

    def get_salary(self):
        return self.salary

def main():
    # Create the employees
    Mateusz = employee("Mateusz Kruk", 113000, 678367732.40)
    Pongo = employee("Pongo", 113077, 801179.01)
    Annie = employee("Annie Walker", 24933, 820.12)
    Eyal = employee("Eyal Lavin", 91781, 2468.00)
    Auggie = employee("Auggie Anderson", 2012, 71940.76)

    #First employee
    print("The first Employee object:")
    Mateusz.print_emp()
    Mateusz.increase_salary(115.15)
    Mateusz.print_emp()

    #Second employee
    print("\nThe second Employee object:")
    Pongo.print_emp()
    Pongo.increase_salary(-50)  #Try to increase with negative amount
    Pongo.print_emp()

    #Third employee
    print("\nThe third Employee object:")
    Annie.print_emp()
    Annie.set_ID_num(654321)
    Annie.set_salary(8.12)
    Annie.print_emp()

    #Fourth employee
    print("\nThe fourth Employee object:")
    Eyal.print_emp()
    Eyal.set_ID_num(809)  #Invalid ID
    Eyal.set_salary(9517.53)
    print(f"Employee 4 has a salary of ${Eyal.get_salary():.2f}")
    Eyal.print_emp()

    #Fifth employee
    print("\nThe fifth Employee object:")
    Auggie.print_emp()
    Auggie.set_salary(-10)  #Invalid salary
    print(f"Employee 5 has an identification number of {Auggie.get_ID_num()}")
    Auggie.print_emp()

main()