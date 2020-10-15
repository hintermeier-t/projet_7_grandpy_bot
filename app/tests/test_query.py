"""
    Script that tests if a query is sent and if a response is get.
"""
from ..py_app.query import Query
import requests
#- Query test class
def test_maps_query(monkeypatch):
    expected_result = {
        "address": "une adresse",
        "lat": 12.134,
        "lng": -30.4135,
        "error": False
    }

    class MockRequestsGet:
        def __init__(self, url, params):
            self.status_code = 200

        def json(self):
            return {
                "candidates": [
                    {
                        "formatted_address": expected_result["address"],
                        "geometry": {
                            "location": {
                                "lat": expected_result["lat"],
                                "lng": expected_result["lng"]
                            }
                        }
                    }
                ]
            }
    monkeypatch.setattr(googlemaps, MockRequestsGet)
    assert google_maps_downloader.find_place("question") == expected_result