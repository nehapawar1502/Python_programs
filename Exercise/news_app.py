import requests
import json

query = input("what type of news do you want : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-03-08&sortBy=publishedAt&apiKey=49d3123370e74ef197c1f117fbcfd38f"

r = requests.get(url)

news = json.loads(r.text)
print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------")