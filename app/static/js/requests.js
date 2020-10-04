let map;
let service;
let infowindow;

function initMap() {
  const initCenter = new google.maps.LatLng(0, 0);
  let infowindow = new google.maps.InfoWindow();
  map = new google.maps.Map(document.getElementById("map"), {
    center: initCenter
    zoom: 15,
  });
  const request = {
    query: "openclassrooms",
    fields: ["name", "geometry"],
  };
  let service = new google.maps.places.PlacesService(map);
  service.findPlaceFromQuery(request, (results, status) => {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
      for (let i = 0; i < results.length; i++) {
        createMarker(results[i]);
      }
      map.setCenter(results[0].geometry.location);
    }
  });
}

function createMarker(place) {
  const marker = new google.maps.Marker({
    map,
    position: place.geometry.location,
  });
  google.maps.event.addListener(marker, "click", () => {
    infowindow.setContent(place.name);
    infowindow.open(map);
  });
}


/*<iframe style="border: 0;" src="{{maps_address}}" width="600" height="450" frameborder="0"></iframe>

<script defer
    src="https://maps.googleapis.com/maps/api/js?libraries=places
        &key=AIzaSyCe3J5f3mogndrirriSvsVwUj0tn2OW6nA&callback=initMap">
</script>*/


