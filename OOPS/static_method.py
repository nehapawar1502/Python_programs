class Math:
   def __init__(self,num):
       self.num = num
       
   def addtonum(self, n):
       self.num = self.num+n
    
   #There is no need to pass the self in the method as a parameter because its not belonging to any instance or class   
   @staticmethod
   def add(a, b):
       return a+b
   
a = Math(5)
print(a.num)
a.addtonum(6)

print(a.num)
print(a.add(5,70)) #we call it by using the instace of the class
print(Math.add(10,30)) #we can call it by using the name of the class because its the static method
    