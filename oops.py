#why we use oops 
'''
oops
1. Classes and objects 

'''

class Person:
    name = "Neha"
    occupation = "Software developer"
    Marks = "90%"
    
    def info(self):
        print(f'name is {self.name} occupation is {self.occupation}')
    
    
p = Person()
q = Person()
p.info()

q.name = "nilu"
q.occupation = "HR"

q.info()


'''
2. Constructor 
'''
class Teacher:
    def __init__(self, n, o):
        print("Hey i am here")
        self.name = n
        self.occ = o
        
    def info(self):
        print(f"{self.name} is a {self.occ}")

t = Teacher("Neha", "sd")
t2 = Teacher("Nilu", "HR")

t.info()
t2.info()


'''
3. Decorators 
   - Decorators takes the function and return that function by changing something.
   - Decorator takes the function as an argument
   - *args takes the arguments as a tuple and *kwargs takes the arguments as a dictionary
'''

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx()
        print("Thanks for using")
    return mfx
    
@greet
def hello():
    print("Hello world")

hello()
# greet(hello)()

