import requests
import json

url = "https://steam-api7.p.rapidapi.com/search"

querystring = {"query":"Grand Theft","limit":"5"}

headers = {
	"x-rapidapi-key": "ad761c6685msh23982c33ec09642p1e22b5jsn8e6e7a7adec0",
	"x-rapidapi-host": "steam-api7.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(response.text)
