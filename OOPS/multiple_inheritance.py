class Employee:
    def __init__(self, name):
        self.name = name 
    def show(self):
        print( f"Name is {self.name}")
    
class Dancer:
    def __init__(self, dance):
        self.dance = dance 
    def show(self):
        print( f"dance is {self.dance}")
        
class DancerEmp(Dancer,Employee):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
        # print f"Name is "+{self.name}+"dance is "+{self.dance5}
        
o = DancerEmp("Katthak","Neha")
print(o.name)
print(o.dance)

print(o.show())

# method resolution order

print(DancerEmp.mro())
    