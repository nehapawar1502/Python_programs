name = ["neha", "dhanu", "janu"]
for a in name:
   print(a)


a = "abhishek"
for i in a:
    print(i)   
    
#  range function 
for k in range(5):
    print(k+1)
    

for i in range(40, 150, 4):
    print(i+5)
    
    
#  for loops with else

for i in range(5):
    print(i)

else:
    print("Sorry no i")
    
    
for i in range(5):
    print("i = ",i)

    if i == 4:
        break  
    # else part will not print if it break the loop
else:
    print(" i am in else")
    

i = 0
while i<=10:
    print(i)
    if i == 5:
        break
    i = i+1
    
else:
    print("hiii")