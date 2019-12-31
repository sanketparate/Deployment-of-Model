import requests

url = 'http://127.0.0.1:5000'
r = requests.post(url,json={"cid": 3034200666,"dayshours":2014117,"room_bed":4,"room_bath":3,"living_meaure":3020,"lot_measure":13457, "ceil":1,"coast":0, "sight":0,"condition":5, "quality":9, "ceil_measure":3020, "basement":0, "yr_built":1956, "yr_renovated":0,"zipcode":98133, "lat":47,"long":-122, "living_measure15":2120, "lot_measure15":7553, "furnished":1, "total_area":16477})

print(r.json())