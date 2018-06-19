import json
import urllib.parse
import requests

with open('GeoCode.txt') as f:
    geocode = f.read().split('\n')

direccion = geocode[0]
address = urllib.parse.quote_plus(direccion)
geokey = geocode[1]
#keyf = urllib.parse.quote_plus(geokey)
url="https://maps.googleapis.com/maps/api/geocode/json?key=%s&address=%s" % (geokey,address)
try:
    response = requests.get(url)
    if not response.status_code == 200:
        print("HTTP error",response.status_code)
    else:
        try:
            response_data = response.json()
        except:
            print("Response not in valid JSON format")
except:
    print("Something went wrong with requests.get")

print("Formatted Address: " + response_data['results'][0]['formatted_address'])
print("Latitud: " + str(response_data['results'][0]['geometry']['location']['lat']))
print("Longitud: " + str(response_data['results'][0]['geometry']['location']['lng']))
