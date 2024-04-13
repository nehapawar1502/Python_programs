import math as m

print(dir(m))

marks  = [50, 67, 47, 59, 90]

# index = 0
# for mark in marks:
#     print(mark)
    
#     if(index == 3):
#         print("Nice")
        
#     index+=1

# by using the enumerate it gives the index 
for index, mark in enumerate(marks):
    print(mark)
    
    if(index == 3):
        print("Nice")
    
    
name  = "Neha"

for index, n in enumerate(name, start = 1):
    print(index, n)
    
    
