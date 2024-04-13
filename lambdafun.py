double = lambda x: x*2

print(double(5))


#above is the same as below

def double(x):
    return x*2

print(double(10))


avg = lambda x,y,z : (x+y+z)/3

print(avg(4,5,6))

# we can pass the function as a argument this is a annonymous function and we can implement this using the lambda functions 
def apply(avg, x, y):
    return 6 + avg(x,y)

print(apply(lambda x,y : (x+y)/3, 10,20))


sum = lambda a,b,c : a+b+c

print(sum(5,5,5))


def annonymousFun(fx, x,y,z):
    return fx(x,y,z)

print(annonymousFun(lambda x,y,z : x+y+z, 10,10,10))