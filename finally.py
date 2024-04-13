def demo():
    try:
        # l1 = [3,6,7,8]
        # print(l1[9])
        a = 10/0
        return 1
        
    except Exception as e:
        print(e)
        return 0
    
    finally:
        print("I am finally")
    # here finally will alway execute instead of that if i write the normal method then will not work  
x = demo()

print(x)

#  Custom errors in pyton

a = int(input("Enter the Number : "))
if (a<5 or a>9):
    raise ValueError("Enter the value between the 5 and 9")