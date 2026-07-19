import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

# 1. Status code — did it work?
print("Status code:", response.status_code)  # 200 = OK
print()