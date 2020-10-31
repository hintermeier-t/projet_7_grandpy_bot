import requests
from ..py_app import query as q

my_query = q.Query("Openclassrooms")
class MockMaps:
    """
    This class will mock a JSON response from a request.
    """
    # mock json() method
    @staticmethod
    def json():
        return {'html_attributions': [],
        'results': [
            {'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
            'geometry': {'location':
                            {'lat': 48.8975156,
                            'lng': 2.3833993}},
            'name': 'Openclassrooms'}],
            'status': 'OK'}


def test_maps_query(monkeypatch):

    def mock_return_m(*args, **kwargs):
        return MockMaps()

    # apply the monkeypatch for requests.get to mock_return
    monkeypatch.setattr(requests, "get", mock_return_m)

    result = my_query.maps_query(query="Openclassrooms")
    assert result == {'html_attributions': [],
    'results': [
        {'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
        'geometry': {'location':
                        {'lat': 48.8975156,
                        'lng': 2.3833993}},
        'name': 'Openclassrooms'}],
        'status': 'OK'}

class MockWiki:
    """
    This class will mock a JSON response from a request.
    """
    # mock json() method
    @staticmethod
    def json():
        return {'pageid': 3120649,
        'title': 'Quai de la Gironde',
        'extract': "Le quai de la Gironde est un quai situé le long du canal \
        Saint-Denis, à Paris, dans le 19e arrondissement.\n\n\n== Situation et \
        accès ==\nIl fait face au quai de la Charente, commence au quai \
        de l'Oise et se termine avenue Corentin-Cariou.\nLa ligne \u2009 du \
        tramway passe sur ce quai.\n\n\n== Origine du nom ==\nLe quai porte le\
         nom que prend le fleuve, la Garonne, après avoir reçu la Dordogne au \
         bec d'Ambès.\n\n\n== Historique ==\nCette voie de l'ancienne commune \
         de La Villette a été classée dans la voirie de Paris par un décret du\
          23 mai 1863 et porte son nom actuel depuis un arrêté du 11 juin 1873\
          .\n\n\n== Bâtiments remarquables et lieux de mémoire ==\nno 11 : \
          emplacement des Entrepôts généraux.\n\n\n== Voir aussi ==\n\n\n=== \
          Articles connexes ===\nListe des voies du 19e arrondissement de Paris\
          \nListe des voies de Paris\n\n\n=== Navigation ===\n Portail de Paris\
             Portail de la route"}
def test_wiki_query(monkeypatch):

    def mock_return_w(*args, **kwargs):
        return MockWiki()

    monkeypatch.setattr(requests, "get", mock_return_w)
    result = my_query.wiki_query(geocode={'lat': 48.8975156,'lng': 2.3833993})
    assert result["pageid"] == 3120649
