import requests

url = 'http://localhost:5000/House Price'
r = requests.post(url,json={'living_measure':820, 'lat':47.7174, 'furnished':1})

print(r.json())