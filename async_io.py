'''Mechanism to run the program concurrently
It executes the parallal tasks 

'''
import time, requests
import asyncio
async def function1():
#    await asyncio.sleep(1)
   URL = "https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg?size=626&ext=jpg&ga=GA1.1.867424154.1713139200&semt=ais"
   response = requests.get(URL)
   open("instagram.ico", "wb").write(response.content)
   print("Function 1")

async def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    print("Function 2")
    
async def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    print("Function 3")
    
    
async def main():
    # await function1()
    # await function2()
    # await function3()
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    
    # print(L)
      
asyncio.run(main())
    