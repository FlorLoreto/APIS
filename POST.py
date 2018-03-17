from io import BytesIO
import pycurl
buf = BytesIO()

def CurlPOST(url, data):
    c = pycurl.Curl()
    b = buf
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()
    html = b.getvalue()
    print (html)
    b.close()
    c.close()
    return html
if __name__ == '__main__':
    CurlPOST('localhost:5000', "hola")

