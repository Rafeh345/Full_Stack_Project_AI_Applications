import requests

url = "http://localhost:5000/analyze-emotion"
data = {
    "text": "I'm really excited about this!"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
