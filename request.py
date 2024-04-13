import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
     print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

data =  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }

headers = {
    'Content-type':'application/json'}

response = requests.post(url,headers = headers,json=data)

print(response.text)
