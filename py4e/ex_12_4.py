import urllib.request
import urllib.parse
import urllib.error

import re

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


# for line in fhand:
#     print(line.decode().strip())

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

sorted_counts = list()
for k, c in counts.items():
    sorted_counts.append((c, k))

print(sorted(sorted_counts, reverse=True))

htmlfile = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in htmlfile:
    line = line.decode().strip()
    url = re.findall('href="(.+)"', line)
    for item in url:
        if len(item) > 1:
            print(item)
