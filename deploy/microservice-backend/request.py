import requests

url = 'http://localhost:8020/api'
response = requests.post(url, json={'day': 10, 'month': 2, 'year': 2020, 'path': 'random_forest_model.joblib'})

if response.status_code == 200:
    print(response.json())
