name = "harry, neha "
print(len(name))
# string slicing it includes the 0 but not 4
print(name[0:5])
#  it will add 0 at starting
print(name[:8])

# negative slicing 
print(name[1:-3])
print(name[1:len(name)-3]) 
# above both are same

print(name[-1:len(name)-3])

print(name[-4:-2])

nm  = "Dhanu"
print(len(nm))
print(nm[-4:-2])


# string operations ---------Strings are immutable in nature we can't change the existing string 

a = "neha!! !! !!"
print(a.lower())
print(a.upper())
print(a.rstrip("!"))
# above function cannot be strip the leading characher it only strip the trailling 
print(a.replace("neha","dhanu"))

print(a.capitalize())
# capatalize convert the first character into upper case and remaining in lower case
print(a.split(" "))
# split converts the the string into the list

print(a.count("neha"))

b = "welcome to the coding"
print(b.find("to"))
print(b.index("to"))