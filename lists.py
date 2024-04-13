l = [1, 2, 3, 4, 1, 1]
print(l)

l.append(8)
print(l)

l.sort()
print(l)

l.sort(reverse = True)
print(l)

l.reverse()
print(l)

print(l.index(8))
print(l.count(1))


# copy method
# by changinf the elements in the m it can directly change the list inside the l

m = l
m[0] = 0
print(m)
print(l)

# below copy function can create the separate copy  for this 

n = l.copy()

n[0] = 100
print(l)
print(n)

# insert at index

l.insert(1,800)
print(l)

o = [70,89,90]
l.extend(o)
print(l)

k = l + o
print(k)