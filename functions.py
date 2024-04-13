def gmean(a,b):
    mean = (a*b)/(a+b)
    return mean

res = gmean(10,5)
print(res)

# greater number program 

def greaterNum(a,b):
    if(a>b):
        return f'{a} is greater'
    else:
        return f'{b} is greater'

result = greaterNum(60,3)
print(result)


# function arguments 
#types of arguments
# 1. default arguments
# 2. Keyword arguments
# 3. Variable length arguments
# 4. Required arguments

def average(a, b, c=1):
    print(a+b+c/2)

average(b=10,a=20)


#  variable length argument
# it will take the list 
def average(*numbers):
    sum =0
    for i in numbers:
        sum = sum+1
    print("Average is", sum/len(numbers))

average(2,4,6,8)