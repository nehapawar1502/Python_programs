def cube(x):
    return x * x * x

l1 = [4,6,8,9]
newList = []

for item in l1:
  newList.append(cube(item))
  
print(newList)

#by using the below map function we cam implement the above 

print(list(map(cube, l1)))
#below is also same
print(list(map(lambda x: x*x*x, l1)))
#it takes the first parameter as a name of the function and second parameter as the name of the list

#FILTER
# it will filter the values and return only those value which is greater than 5
def filter_fun(a):
    return a>5

print(list(filter(filter_fun, l1)))


