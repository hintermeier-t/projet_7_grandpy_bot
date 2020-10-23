import requests
from ..py_app import query as q
class MockMaps:
"""
    This class will mock a JSON response from a request.
"""
    # mock json() method
    @staticmethod
    def json():
        return {"json_key": "json_resp"}


def test_maps_query(monkeypatch):

    def mock_return_m(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_return
    monkeypatch.setattr(requests, "get", mock_return_m)

    result = q.maps_query("Openclassrooms")
    assert result["json_key"] == "json_resp"

class MockWiki:
"""
    This class will mock a JSON response from a request.
"""
    # mock json() method
    @staticmethod
    def json():
        return {"json_key": "json_res
def test_wiki_query(monkeypatch):

    def mock_return_w(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_return_w)
    result = q.maps_query("0|0")
    assert result["json_key"] == "json_resp"
