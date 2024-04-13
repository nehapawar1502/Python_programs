try:
    print("hello")
except Exception as e:
    print(e)


try:
    print("hii")
    
except:
    print("except")
    
    
try:
    
    l1 = [2,5,7,8]
    print(l1[9])
    # code
except ValueError:
    print("value error")
except IndexError:
    print("IndexError")

finally:
    print("This is finally block")
    
    

    
    
    
    
