from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

from app import app

app.config['GOOGLEMAPS_KEY'] = 'AIzaSyDXtCfWA1EuXPc4geNQTm2NsIb8xllcCac'


# Initialize the extension
GoogleMaps(app)
map = Map(
    identifier="view-side",
    lat=30.577541,
    lng=-97.652797,
    zoom=16,
    style="height:100%; width:100%"
)
