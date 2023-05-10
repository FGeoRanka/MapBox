import mapboxgl from 'mapbox-gl';

mapboxgl.accessToken = 'YOUR_ACCESS_TOKEN_HERE';

var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-122.4194, 37.7749],
  zoom: 13
});