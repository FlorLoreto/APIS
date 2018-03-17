import requests

latitude = 40.4167754
longitude = -3.7037902


payload1 = {
            'v': '20180303',
            'll': str(latitude)+','+str(longitude),
           'client_id': 'WYVIS2GYW3U0F4PV0XYBNHDXI0C3OECKSHJWG4CVVOCLA10D',
           'client_secret': 'EYDDNGVVV1WY2IEIWMEJK2YZ5TGQS5OAGHVAWFD1DLYK31S2',
            'city': 'Madrid',
            'zip': '28033',
            'radius': 500,
            'query': 'restaurante'
           }
print (payload1)
URL1 = ('https://api.foursquare.com/v2/venues/search')


def local():
    r1 = r1equests.get(Ur1L1, params=payload1)
    return r1


if __name__ == "__main__":
    resto = local().json()
    print(resto)
    print('resto \n', resto['response']['venues'][0]['name'])
    print('\n Teléfono', resto['response']['venues'][0]['contact']['phone'])
