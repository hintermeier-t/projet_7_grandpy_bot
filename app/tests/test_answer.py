import requests

S = requests.Session()

URL = "https://fr.wikipedia.org/w/api.php"

PARAMS = {
    "action": "opensearch",
    "namespace": "0",
    "search": "Nicolas Sarkozy",
    "limit": "5",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)