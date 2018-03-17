# importing the requests library
import requests  # Biblioteca HTTP usda
from PIL import Image

im = Image.open(r'C:\Users\rufus\Pictures\FOTODEBORAH.JPG')
payload = {'key': 'AIzaSyCaddcyqqbJJroAZHhsG60xQnfMl5HECUQ',
           'address': ''}


def caracter(text):
    for c in [' ', ',']:
        if c in text:
            text = text.replace(c, "+")
    return text


def getGeocodeLocation(sitio):
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=Madrid+España&key=AIzaSyCaddcyqqbJJroAZHhsG60xQnfMl5HECUQ
    payload['address'] = caracter(sitio)
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
    # latitude = result['results'][0]['geometry']['location']['lat']
    # longitude = result['results'][0]['geometry']['location']['lng']
    # print(r.text)
    return r


payload1 = {
    'v': '20180303',
    'll': '',
    'client_id': 'WYVIS2GYW3U0F4PV0XYBNHDXI0C3OECKSHJWG4CVVOCLA10D',
    'client_secret': 'EYDDNGVVV1WY2IEIWMEJK2YZ5TGQS5OAGHVAWFD1DLYK31S2',
    'query': ''
}

URL1 = ('https://api.foursquare.com/v2/venues/search')


def local():
    r1 = requests.get(URL1, params=payload1)
    return r1


if __name__ == "__main__":
    sitio = input("What's your location? ")
    meal = input("What's your favorite food?")
    madrid = getGeocodeLocation(sitio).json()
    # print('Madrid', madrid)
    latitude = madrid['results'][0]['geometry']['location']['lat']
    longitude = madrid['results'][0]['geometry']['location']['lng']
    print(latitude)
    print(longitude)
    payload1['ll'] = str(latitude) + ',' + str(longitude)
    payload1['query'] = meal
    resto = local().json()
    # print(resto)
    try:
        print('Resto \n', resto['response']['venues'][0]['name'])
        print('\n Teléfono', resto['response']['venues'][0]['contact']['phone'])
    except:
        IndexError
        print ('no hay')
        pass
    print(im.format, im.size, im.mode)
    im.show()
