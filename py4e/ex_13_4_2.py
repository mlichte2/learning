import urllib.request
import urllib.error
import urllib.parse

import xml.etree.ElementTree as ET

endpoint = input('Enter URL: ')
response = urllib.request.urlopen(endpoint).read()

xml = ET.fromstring(response)
lst = xml.findall('comments/comment')

sum = 0

for comment in lst:
    print(comment.find('name').text, comment.find('count').text)
    sum += int(comment.find('count').text)

print(sum)
