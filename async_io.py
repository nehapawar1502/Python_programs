'''Mechanism to run the program concurrently

'''
import time, re
import asyncio
async def function1():
   await asyncio.sleep(1)
   URL = "https://instagram.com/favicon.ico"
   response = requests.get(URL)
   open("instagram.ico", "wb").write(response.content)
   print("Function 1")

async def function2():
    await asyncio.sleep(1)
    print("Function 2")
    
async def function3():
    await asyncio.sleep(1)
    print("Function 3")
    
    
async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    
    print(L)
      
asyncio.run(main())
    