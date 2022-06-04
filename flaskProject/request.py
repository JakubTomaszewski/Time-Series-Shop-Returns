import requests

url = 'http://localhost:5000/api'
r = requests.post(url,json={'day':10, 'month':2, 'year':2020})
print(r.json())
