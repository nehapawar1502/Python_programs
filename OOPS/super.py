'''
super keyword is used to call the parent methods in the child class
super keyyword is used to refer the parent class

'''

class Pclass:
    def p_method(self):
        print("parent class")
        
class Cclass(Pclass):
    
    def p_method(self):
        print("hii neha")
        super().p_method()
    def c_method(self):
        print("child class")
        super().p_method()
    
        
child_obj = Cclass()
child_obj.c_method()
