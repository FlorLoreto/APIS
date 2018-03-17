# Programa que obtiene de google maps las coordenadas de una población
#
import requests  # Biblioteca HTTP usda

# Los parámetros de la consulta se pasan como diccionario
payload = {'key': 'AIzaSyCaddcyqqbJJroAZHhsG60xQnfMl5HECUQ',
           'address': ''}
URL = 'https://maps.googleapis.com/maps/api/geocode/json'


def caracter(text):
    for c in [' ', ',']:
        if c in text:
            text = text.replace(c, "+")
    return text


def getGeocodeLocation(sitio):
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=Madrid+España&key=AIzaSyCaddcyqqbJJroAZHhsG60xQnfMl5HECUQ
    payload['address'] = caracter(sitio)
    r = requests.get(URL, params=payload)
    # latitude = result['results'][0]['geometry']['location']['lat']
    # longitude = result['results'][0]['geometry']['location']['lng']
    print(r.text)
    return r


# 4Squares
URL1 = ('https://api.foursquare.com/v2/venues/search')
payload1 = {
    'v': '20180303',
    'll': '',
    'client_id': 'WYVIS2GYW3U0F4PV0XYBNHDXI0C3OECKSHJWG4CVVOCLA10D',
    'client_secret': 'EYDDNGVVV1WY2IEIWMEJK2YZ5TGQS5OAGHVAWFD1DLYK31S2',
    'city': 'Madrid',
    'zip': '28033',
    'radius': 500,
    'query': 'restaurante'
}
def local():
    r1 = requests.get(URL1, params=payload1)
    return r1
if __name__ == "__main__":
    madrid = getGeocodeLocation('Madrid,España').json()
    print('Madrid', madrid)
    latitude = madrid['results'][0]['geometry']['location']['lat']
    longitude = madrid['results'][0]['geometry']['location']['lng']
    print(type(latitude), latitude)
    print(type(latitude, longitude)
    payload1['ll': str(latitude) + ',' + str(longitude)]
    print('resto \n', resto['response']['venues'][0]['name'])
    print('\n Teléfono', resto['response']['venues'][0]['contact']['phone'])
