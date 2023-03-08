import urllib.request
import urllib.error
import urllib.parse

from bs4 import BeautifulSoup


def find_name():
    url = input('enter url: ')
    count = int(input('count: '))
    position = int(input('position: '))
    while count > 0:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        links = soup('a')
        link = links[position - 1]
        url = link.get('href', None)
        count -= 1
        print('Retrieving:', url)


find_name()
