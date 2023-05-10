import os
import json
import requests
import numpy as np
import folium
from folium import plugins

# HERE Routing API credentials
HERE_APP_ID = "YOUR_APP_ID"
HERE_APP_CODE = "YOUR_APP_CODE"

# Center point (Zagreb Cathedral)
center = [45.8144, 15.9779]

# Isochrone time intervals (in minutes)
intervals = [10, 20, 30, 40]

# HERE Routing API endpoint
url = "https://route.api.here.com/routing/7.2/calculateisoline.json"

# Create a map centered at the center point
map = folium.Map(location=center, zoom_start=13)

# Create a feature group for the isochrones
isochrones = folium.FeatureGroup(name="Isochrones")

# Create an icon to mark the center point
icon = folium.Icon(color='red', icon='info-sign')

# Add a marker for the center point
folium.Marker(location=center, icon=icon, tooltip="Center point").add_to(map)

# Iterate over the time intervals
for t in intervals:
    # Create a request payload for the isochrone
    payload = {
        "app_id": HERE_APP_ID,
        "app_code": HERE_APP_CODE,
        "mode": "fastest;car;traffic:disabled",
        "start": f"geo!{center[0]},{center[1]}",
        "rangetype": "time",
        "range": t * 60,
        "departure": "now"
    }

    # Send the request to the HERE Routing API
    response = requests.get(url, params=payload)

    # Parse the response as GeoJSON
    feature_collection = json.loads(response.text)

    # Create a feature for the isochrone and add it to the feature group
    feature = folium.GeoJson(feature_collection, name=f"{t} min")
    feature.add_to(isochrones)

# Add the isochrones feature group to the map
isochrones.add_to(map)

# Add a layer control to the map
folium.LayerControl().add_to(map)

# Display the map
map
