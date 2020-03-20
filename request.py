import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':200,})
print(r.json())