'''
Access modifiers - All the variables and methods in the python are by default public 
1. private - __name is a private access specifier

2.__ is used for name mangling-- name mangling is the technique used to protect class private subclass private attribute from accidently overwrite

3 Protected is used to describe the member of the class that is indended to be accessed only by the class itself and its subclasses.
by using the single _ 
'''


class Employee:
    def __init__(self):
        self.__name = "Neha"

e1 = Employee()
# print(e1.__name) It cannot be accessed directly but can access indirectly.

# print(e1._Employee__name)
        
