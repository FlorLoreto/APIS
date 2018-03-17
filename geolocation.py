import json
from pprint import pprint

import requests

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "AIzaSyCaddcyqqbJJroAZHhsG60xQnfMl5HECUQ"
    locationString = inputString.replace(" ", "+")
    #url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (locationString, google_api_key))
    URL=('https://maps.googleapis.com/maps/api/geocode/json?address=locationString&key=AIzaSyCaddcyqqbJJroAZHhsG60xQnfMl5HECUQ')
    #h = httplib2.Http()
    h1 = requests.get(url=URL)
    # extracting data in json format
    data = h1.json()
    data1=h1.text
    # extracting latitude, longitude and formatted address
    # of the first matching location
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']
    # latitude = result['results'][0]['geometry']['location']['lat']
    # longitude = result['results'][0]['geometry']['location']['lng']
    # return (latitude,longitude)
    #h2=json.loads(h1)
    pprint(h1)
    pprint(h2)




dallas = getGeocodeLocation("Madrid")
dir(dallas)

