import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup

import ssl

# ignore ssl certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter domain - ")
html = urllib.request.urlopen(url, context=ctx).read()
# BS deals with converting utf-8 to unicode, hence no decoding
soup = BeautifulSoup(html, 'html.parser')

# retrieve all anchor tags

tags = soup('a')
for tag in tags:
    print(tag)
    print(tag.get('href', None))
