class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
neha  = Employee("neha", 23)
harry = Programmer("Harry", 56, "Java")
print(harry.name)
print(harry.id)
print(harry.lang)