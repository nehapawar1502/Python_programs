'''
Dunder methods in the python:
1. len
2. str


'''

class Employee:
    
    def __init__(self, name):
        self.name = name
        

    def __len__(self):
        i = 0
        for n in self.name:
            i = i+1
            
        return i 
    
    def __str__(self):
        return f"this is the name of the employee {self.name}"

e = Employee("name")

print(e.name)
print(str(e))
print(len(e))
        