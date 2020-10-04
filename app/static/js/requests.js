let map: google.maps.Map;

function initMap(): void {
  map = new google.maps.Map(document.getElementById("map") as HTMLElement, {
    center: { lat: 48.8588377, lng: 2.2770202 },
    zoom: 5,
  });
}
function google_request(ask){
    var request = new XMLHttpRequest();
    request.open("GET", "http://url-service-web.com/api/users");
    request.send();
}