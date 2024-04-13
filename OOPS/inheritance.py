class Employee:
    def __init__(self, name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"Name is {self.name}, id is {self.id} ")
        
#Single inheritance    
class Programmer(Employee):
    def show(self):
        print("This is the Programmer class....")
        
class MiniProgrammer(Programmer):
    def mini(self):
        print("This is the mini programmer function")
        
        
e = Employee("Neha", 20)
e.showDetails()    
e1 = MiniProgrammer("Nilu", 19)
e1.showDetails()
e1.show()
e1.mini()





    
    