import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()  # List of dictionaries
    for post in posts[:3]:   # Display the first 3 posts
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print(f"Error: {response.status_code}")
