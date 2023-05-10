const mapboxClient = require('mapbox');

const accessToken = 'pk.eyJ1IjoiZmdlb3JhbmthIiwiYSI6ImNsaDZpYnRndDA2Z3AzcW5zN3Z6eXpkdnUifQ.zCGgF9WHj4NraRMnm_q0lg';
const client = new mapboxClient(accessToken);

const options = {
  profile: 'walking',
  contours_minutes: [5, 10, 15],
  polygons: true
};

const coordinates = [15.9779844, 45.8131613];

client.isochrone(options, coordinates, (err, res) => {
  if (err) throw err;
  console.log(res);
});