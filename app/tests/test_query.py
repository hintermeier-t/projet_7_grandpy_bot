"""
    Script that tests if a query is sent and if a response is get.
"""
from ..py_app.query import Query
import requests
#- Query test class
class TestQuery:
    def test_maps_response (monkeypatch):
        address = '10 Quai de la Charente, 75019 Paris, France'
        geocode = {'lat': 48.8974305, 'lng': 2.3835276}

        def mockreturn(requests):
            return address, geocode
        monkeypatch.setattr(requests, 'get',mockreturn)

#- Google Maps locate the city

#- We look for the location on Wikipedia
