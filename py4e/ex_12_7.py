import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup

# this is over http so no need to import ssl

url = input('Enter domain -- ')
# url = 'http://py4e-data.dr-chuck.net/comments_1719803.html'

http = urllib.request.urlopen(url).read()


soup = BeautifulSoup(http, "html.parser")

tags = soup('span')

answer = 0

for tag in tags:
    answer += int(tag.contents[0])

print(answer)
