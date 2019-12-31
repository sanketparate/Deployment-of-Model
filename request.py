import requests

url = 'http://127.0.0.1:5000/House Price'
r = requests.post(url,json={'living_measure':820, 'lat':47, 'furnished':1})

print(r.json())