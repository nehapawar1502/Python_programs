
'''
dir
__dict__

help

'''

x = [2,5,7]
print(x)
print(dir(x))

print(x.__add__)


class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
p = Person("neha ", 700000)
print(p.__dict__)

print(help(Person))