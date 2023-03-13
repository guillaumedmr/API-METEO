import folium
import json
import requests

url = "https://france-geojson.gregoiredavid.fr/repo/regions.geojson"
response = requests.get(url)
data = json.loads(response.text)

m = folium.Map(location=[46.00, 2.00], zoom_start=6)

for feature in data["features"]:
    folium.GeoJson(feature).add_to(m)
    
m.save("index.html")