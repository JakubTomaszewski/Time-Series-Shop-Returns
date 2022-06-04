import requests

url = 'http://localhost:6000/api'
response = requests.post(url, json={'day': 10, 'month': 2, 'year': 2020})

if response.status_code == 200:
    print(response.json())
