# duplicate values are not allowed in this , 
# its not maintaining the order of the data
# we can not change the value of set items its unchangeable

s = {
2, 4, 5, 8, 8, 2
}

print(s)

for s1 in s:
    print(s1)
    
    
# methods of sets 


s1 = {1,5,6,8,9}
s2 = {10,3,7,9}
print(s1.union(s2))

print(s1.intersection(s2))
s3 = s1.update(s2)
print(s3)

# symentric difference (a union b) - (a intersection b)

