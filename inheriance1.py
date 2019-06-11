
class Person:
     
    def __init__(self, name):
        self.name = name
 
    def getName(self):
        return self.name
 
    def isperson(self):
        return False
 



class Employee(Person):
 
    def isEmployee(self):
        return True
 
emp = Person("kaushal")  # An Object of Person
print emp.getName(), emp.isperson()
 
emp = Employee("yashika") # An Object of Employee
print emp.getName(), emp.isEmployee()
