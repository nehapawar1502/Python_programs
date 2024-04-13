# tuples - we cannot change the tuples
tup = (1, 5)
print(type(tup), tup)

#  in the following case python will consider it as a integer instead of tuple 
tup = (1)
print(type(tup), tup)
# we need to add semicolon after one integer for considering it as a tuple
tup = (1,)
print(type(tup), tup)

tup2 = (45, 56, 7, "neha", True)
print(tup2)


tup3 = tup2[2:4]
print(tup3)

# methods of tuples we need to convert the tuple into the list first then we can add the 
tup4 = (23, 56, 78, 20,10)
li1 = list(tup4)
li1.append(88)
tup4 = tuple(li1)
print(tup4)

# tuple methods
