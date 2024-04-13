from functools import reduce

list1 = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y, list1)

print(sum)


list2 = [2,4,7,9,6]

#example 2
def sum(x,y):
    return x+y

sum = reduce(sum,list2)


#is == difference
# is comapres the exact loaction of the memory and == compares the values

a = 4
b = 4

print(a == b)
print(a is b) # it will give the true value because both 4 are getting met]mory at same place because it is constant


c = [1, 2, 4]
d = [1, 2, 4]

print(c == d) # 
print(c is d) # it is giving the false because list are mutable its values can change

e = (1,3)
f = (1,3)

print(e is f)
print(e == f)

