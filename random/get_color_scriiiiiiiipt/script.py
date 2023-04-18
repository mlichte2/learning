import requests

from bs4 import BeautifulSoup

import urllib.parse

url = input('Enter URL > ')
if len(url) < 1:
    url = 'https://fastapi.tiangolo.com/uk/deployment/deta/'

try:
    response = requests.get(url, allow_redirects=True)
    print(response.status_code)
except:
    print(response.status_code)

url_parts = urllib.parse.urlparse(url)
result = "{uri.scheme}://{uri.netloc}/".format(uri=url_parts)
base_url = result

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all('link')
print(links)

css_urls = []

for link in links:
    if link['rel'][0] != 'stylesheet':
        continue
    else:
        css_urls.append(link['href'])

normalized_css_urls = []

for css_link in css_urls:
    if css_link.startswith('http'):
        continue
    elif css_link.count('../') > 0:
        css_link = base_url + css_link.replace("../", "")
        print(css_link)
    else:
        css_link = base_url + css_link
        print(css_link)
    normalized_css_urls.append(css_link)


print(normalized_css_urls)
