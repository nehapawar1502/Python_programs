'''
Instance variables vs class variables 

'''

class Employee:
    # class variables are shareable they are same for the all the instance of the class
    company_name  = "Nakshatra Technohub"
    noOfEmp = 0
    def __init__(self, name):
        # these are the instance variable they are associated with the class
        self.name = name
        self.raise_amt = 0.3
        Employee.noOfEmp += 1
    def show(self):
        print(f"this is name {self.name} and raise amount is {self.raise_amt} and company is {self.company_name} of sized {Employee.noOfEmp}")
        
e1 = Employee("Neha")
e1.show()
Employee.show(e1)#both are same 

e2 = Employee("Nilu")
# we can change the value of the instance variable
e2.raise_amt = e2.raise_amt + 3
e2.show()

# changing the value of the class variable and we change this because it searches for the instance variable first 
#  if it does not get the instance variable value for this then it assigns the class variable value 
e3 = Employee("Divya")
e3.company_name = "google"
e3.show()

