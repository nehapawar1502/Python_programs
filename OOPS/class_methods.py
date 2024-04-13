
'''
Classes are used to build the custom data types 

it can change the class variables 
'''

class Employee:
    company = "Apple"
    def show(self):
        print(f"The company is : {self.company}")
#below method directly change the company name which is the class method we can't directly changed it
    @classmethod   
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        
e1 = Employee()
e1.show()
e1.changeCompany("Tesla")
e1.show()

print(Employee.company)

'''class methods can be used as the alternate constructors 


'''

class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
e =Emp("Neha", 8000000)
print(e.name)
print(e.salary)

data = "nulu-5000000"
e2 = Emp(data.split("-")[0],data.split("-")[1])

print(e2.name)
print(e2.salary)

''' In the above code we are having the different type of data to be handle so how can we handle this
    below is the alternate technique to handle this
'''


class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod    
    def fromStr(self,string):
        return self(string.split("-")[0], string.split("-")[1])
    
    @classmethod
    def fromData(cls, string):
        return cls(string.split(":")[0],string.split(":")[1] )
        
e =Emp("Neha", 8000000)
print(e.name)
print(e.salary)

data = "nilu-5000000"
e2 = Emp.fromStr(data)

print(e2.name)
print(e2.salary)

data2 = "Dhanu:4000000"

e3 = Emp.fromData(data2)

print(e3.name)
print(e3.salary)
        
        
        
        