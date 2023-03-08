import urllib.request
import urllib.parse
import urllib.error
import json

import ssl

# ignore ssl certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
apikey = None  # redacted

while True:
    address = input('Enter location: ')

    if len(address) < 1:
        break

    url = serviceurl + \
        urllib.parse.urlencode({'address': address}) + f"&key={apikey}"
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    headers = dict(uh.getheaders())
    print(headers)

    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Faiure To Retrieve ====')
        print(data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
