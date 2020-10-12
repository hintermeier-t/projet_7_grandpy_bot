#- Default modules
import os

#- Custom modules
import parser

#- Pypi modules
import requests
import googlemaps

class Query:

    def __init__(self,query):

        self.query = query
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

    def wiki_query(self):
        url = "https://fr.wikipedia.org/w/api.php"
        address = Parser(self.formatted_address)
        url = "https://fr.wikipedia.org/w/api.php"
        page_params = {
                            "action": "query",
                            "prop": "extracts",
                            "explaintext": 1,
                            "titles": address.string,
                            "format": "json"
        }
        extract_params = {
                        "action": "query",
                        "prop": "extracts",
                        "explaintext": 1,
                        "titles": address.string,
                        "format": "json"
        }
