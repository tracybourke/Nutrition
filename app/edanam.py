


app_id = "1c151feb"
app_key = "36787056f538f7a336fcb7b8c67f39c7"

#url = f"https://api.edamam.com/api/v2/recipies.json?app_id={app_id}&app_key={app_key}"
#print(url)


query = "coffee"

url = f"https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}"
print(url)

import requests
import json

url = 'https://api.edamam.com/search?q=' + query + '&app_id=' + app_id + '&app_key=' + app_key

r = requests.get(url)
data = json.loads(r.text)
print(type(data))
print(data)

results = data["hits"]
print(type(results))
print(len(results))

from pprint import pprint

pprint(results[0])