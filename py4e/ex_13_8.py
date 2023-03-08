import urllib.error
import urllib.parse
import urllib.request

import json

url = input('Enter a url: ')
url = urllib.request.urlopen(url)

data = url.read().decode()

json = json.loads(data)

sum = 0
for item in json["comments"]:
    sum += item["count"]

print(sum)
