#increment loop
i = 0
while(i <= 3):
    print(i)
    i = i+1
    
count = 5


# decrement loop else statement is exected after the ending of the while loop.
# There is no do while loop in python  
while( count >=0):
    print (count)
    count = count - 1
else:
    print("I am inside else")
    
    
#Break and continue

#break will break the loop
for i in range(12):
    if(i==10):
        break
   
    print(" 5 * ", i+1 , "=", 5 * (i+1))
    
print("outside the loop")


#continue will skip the iteration

for i in range(12):
    if(i==10):
        continue
    print(" 6 * ", i+1 , "=", 10 * (i+1))
    
    
#Do while loop - it will execute at least one time 

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break
    
    