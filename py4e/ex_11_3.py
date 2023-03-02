# You will extract all the numbers in the file and compute the sum of the numbers.

import re

fhand = open('regex_sum_1719801.txt')

numlist = list()

for line in fhand:
    line = line.strip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) >= 1:
        for number in numbers:
            number = int(number)
            numlist.append(number)

print(sum(numlist))
