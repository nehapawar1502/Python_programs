from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return 5*n
    
print(fx(10))
print("done for 10")
print(fx(7))
print("done for 7")
print(fx(5))
print("done for 5")
print(fx(11))
print("done for 11")

print(fx(10))
print("done for 10")
print(fx(7))
print("done for 7")
print(fx(5))
print("done for 5")
print(fx(11))
print("done for 11")