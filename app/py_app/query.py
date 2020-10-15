#- Default modules
import os

#- Custom modules
import parser

#- Pypi modules
import requests
import googlemaps

class Query:
    def __init__(self,query):
        tmp_query = parser.Parser(query)
        self.query = tmp_query.string
        self.address = None
        self.geocode = None
        self.wiki_decription = None

    def maps_query(self):
        #- Opening the API client with Google API key
        gmaps = googlemaps.Client(key=os.getenv("GMAPS_API_KEY"))
        #- Search for every places that match the query
        place = gmaps.find_place(input=self.query,
                                input_type="textquery",
                                fields=["formatted_address"],
                                language="fr")
        #- Get the first address (from the most relevant place)
        self.address = place["candidates"][0]["formatted_address"]
        self.geocode = gmaps.geocode(self.address)
        self.geocode = self.geocode[0]["geometry"]["location"]

    def wiki_query(self):
        #- Format the geocode to request it
        geocode_str = (str(self.geocode["lat"]) +
            "|"+
            str(self.geocode["lng"]))
        url = "https://fr.wikipedia.org/w/api.php"
        #- The first wikipedia request to find a page near the location
        page_params = {
            "action": "query",
            "list": "geosearch",
            "gscoord": geocode_str,
            "gsradius": 1000,
            "gslimit": 10,
            "format": "json"
        }
        page_request = requests.get(url, page_params)

        #- Get the page id for the second request
        page_id = str(page_request.json()["query"]["geosearch"][0]["pageid"])
        extract_params = {
            "action": "query",
            "prop": "extracts",
            "explaintext": 1,
            "pageids": page_id,
            "format": "json"
        }
        extract_request = requests.get(url, extract_params)

        #- Gathering the extract and the page link for GrandPy's answer
        self.extract = (extract_request.json()['query']['pages']
            [page_id]['extract'])
        self.link = ('https://fr.wikipedia.org/wiki/'+str(extract_request.json()
            ['query']['pages'][page_id]['title']).replace(' ','_'))

    def make_query():
        self.maps_query()
        self.wiki_query()