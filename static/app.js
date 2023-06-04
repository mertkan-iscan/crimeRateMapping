let map;
let directionsService;
let directionsRenderer;
let originMarker;
let destinationMarker;

function initMap() {
  directionsService = new google.maps.DirectionsService();
  directionsRenderer = new google.maps.DirectionsRenderer();

  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 37.7749, lng: -122.4194 },
    zoom: 10,
  });

  directionsRenderer.setMap(map);

  // Add event listeners for map clicks
  map.addListener('click', (event) => {
    const latLng = event.latLng;
    if (!originMarker) {
      placeOriginMarker(latLng);
    } else if (!destinationMarker) {
      placeDestinationMarker(latLng);
    }
  });

  const getDirectionsButton = document.getElementById('get-directions');
  getDirectionsButton.addEventListener('click', getDirections);
}

function placeOriginMarker(latLng) {
  originMarker = new google.maps.Marker({
    position: latLng,
    map: map,
    label: 'A',
  });
  document.getElementById('origin').value = `${latLng.lat()}, ${latLng.lng()}`;
}

function placeDestinationMarker(latLng) {
  destinationMarker = new google.maps.Marker({
    position: latLng,
    map: map,
    label: 'B',
  });
  document.getElementById('destination').value = `${latLng.lat()}, ${latLng.lng()}`;
}

function getDirections() {
  const origin = document.getElementById('origin').value;
  const destination = document.getElementById('destination').value;

  if (!origin || !destination) {
    alert('Please select both origin and destination');
    return;
  }

  directionsService.route(
    {
      origin: origin,
      destination: destination,
      travelMode: 'DRIVING',
    },
    (result, status) => {
      if (status === 'OK') {
        directionsRenderer.setDirections(result);
        // Remove origin and destination markers
        if (originMarker) {
          originMarker.setMap(null);
          originMarker = null;
        }
        if (destinationMarker) {
          destinationMarker.setMap(null);
          destinationMarker = null;
        }
      } else {
        alert('Error getting directions: ' + status);
      }
    }
  );
}
