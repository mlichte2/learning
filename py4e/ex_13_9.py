import urllib.error
import urllib.parse
import urllib.request

import json

location = input('Enter a location: ')

url = 'http://py4e-data.dr-chuck.net/json?' + \
    f"{urllib.parse.urlencode({ 'address': location })}" + "&key=42"


data = urllib.request.urlopen(url).read().decode()

jsondata = json.loads(data)

print(jsondata["results"][0]["place_id"])
