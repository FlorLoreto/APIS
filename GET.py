import pycurl
from io import BytesIO

buf = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, 'https://maps.googleapis.com/maps/api/geocode/json?address=maputo+mozambique&key=AIzaSyCaddcyqqbJJroAZHhsG60xQnfMl5HECUQ')
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()

print (buf.getvalue())
buf.close()
