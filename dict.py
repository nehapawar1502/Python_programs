# key value pairs, dictionary is in order

dict = {
    "name": "Neha",
    "id": 899
}

print(dict)

print(dict['name'])

info = {
    "name" : "Neha",
    "Id": 100,
    "marks": 600
}

for key in info.keys():
    print(key)
    
for value in info.values():
    print(value)
    
    
    
print(info.items())

# methods

# update adds the values od second dict into first dict
ep1 = {20 : 300, 88:10, 10:22}
ep2 = {30:100, 3:20}

ep1.update(ep2)  
print(ep1)


ep2.clear()
print(ep2)

ep1.pop(20)
print(ep1)

ep1.popitem()
print(ep1)


del ep1[10]

print(ep1)


