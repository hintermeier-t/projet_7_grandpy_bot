# coding:utf-8
"""
The query module contains the Query class.
It is used to gather the data in order to answer the user's question.
"""
# - Default modules
import os

# - Custom modules
from .parser import Parser

# - Pypi modules
import requests


class Query:
    """
    This class manages the requests by :
    1. Parsing the query sent by a user;
    2. Sending the parsed query in a request to google, then wikipedia;
    3. Ordering the needed data.

    Attributes:
    -----------
    :self.query(string): The user query (every stop word removed)
    :self.response (dict): the requests answers to return.

    Methods:
    --------
    :maps_query(self,query): Send a request to Google Maps to find a place.
    :wiki_query(self,geocode): Send a request to French Wikipedia to find
    a wiki page near the place.
    :make_query(self,query): calls both methods, and links maps_query's
    geocode to wiki_query method.
    """
    def __init__(self, query):
        parsing_query = Parser(query)
        self.query = parsing_query.string
        self.response = self.make_query(self.query)

    def maps_query(self, query):
        """
        Search for every places that match the query arg.
        """
        maps_url = (
            "https://maps.googleapis.com/maps/api/place/textsearch/json?"
            + "query="
            + query
            + "&key="
            + os.getenv("GMAPS_API_KEY")
        )

        return requests.get(maps_url).json()

    def wiki_query(self, geocode):
        """
        Send the Wikipedia request searching by location (geocode arg).
        """
        # - Format the geocode to request it
        geocode_str = str(geocode["lat"]) + "|" + str(geocode["lng"])
        url = "https://fr.wikipedia.org/w/api.php"
        # - The first wikipedia request to find a page near the location
        page_params = {
            "action": "query",
            "list": "geosearch",
            "gscoord": geocode_str,
            "gsradius": 1000,
            "gslimit": 10,
            "format": "json",
        }
        page_request = requests.get(url, page_params)

        # - Get the page id for the second request
        page_id = str(page_request.json()["query"]["geosearch"][0]["pageid"])
        extract_params = {
            "action": "query",
            "prop": "extracts",
            "explaintext": 1,
            "pageids": page_id,
            "format": "json",
        }
        return (requests.get(url, extract_params)
            .json()["query"]["pages"][page_id])

    def make_query(self, query):
        """
        Send both maps and wiki queries (using query arg)and return a dict
        containing the needed data.
        """
        maps = self.maps_query(query)
        wiki = self.wiki_query(
            maps["results"][0]["geometry"]["location"])

        return {
            "geocode": maps["results"][0]["geometry"]["location"],
            "address": maps["results"][0]["formatted_address"],
            "extract": wiki["extract"][: wiki["extract"].find("\n")],
            "link": (
                "https://fr.wikipedia.org/wiki/"
                + str(wiki["title"]).replace(" ", "_")
            ),
        }
