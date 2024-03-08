import requests

url = 'http://localhost:5000/detect'
data = {'text': 'Hello, how are you?'}

response = requests.post(url, json=data)
print(response.json())


url = 'http://localhost:5000/translate'
data = {
    'text': 'Hello, how are you?',
    'target_language': 'spanish'
}

response = requests.post(url, json=data)
print(response.json())
