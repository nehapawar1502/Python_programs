
#yield- it will create a values at the moment when it required
def my_generator():
    for i in range(20):
        i=i+5
        yield i
        
        
gen  = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)
