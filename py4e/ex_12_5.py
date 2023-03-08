# parsing web pages
# why scrape?

# to-do build scraper for https://www.chamonixhouse.com/shop-all for 'soviet military poster'

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
