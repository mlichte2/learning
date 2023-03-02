# matching and extracting data

import re

x = "My 2 favorite numbers are 19 and 42"

regex1 = '[0-9]+'

y = re.findall(regex1, x)
print(y)

# prints ['2', '19', '42']

y = re.findall('[AEIOU]', x)
print(y)

# nothing returned since there are no capital vowels

# greedy matching -- greedy returns the largest string possible

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)  # ['From: Using the :']

y = re.findall('^F.+?:', x)  # ? means non greedy and gets the shortest string
print(y)  # ['From:']

# find email address

hand = open('mbox-short.txt')
text = hand.read()

# emails = re.findall('\S+@\S+', text)

# returns ['stephen.marquard@uct.ac.za', '<postmaster@collab.sakaiproject.org>', 'source@collab.sakaiproject.org', 'stephen.marquard@uct.ac.za']

# lets be more specific
emails = re.findall('From: (\S+@\S+)', text)
print(emails)
# returns ['stephen.marquard@uct.ac.za']
# so we are searching for emails that only come from the send line and extracting just the stuff that matches
# the regex in ()

text = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# lets get the email domain

# extact after @ sign, any non blank character, zero or more times
y = re.findall('@([^ ]*)', text)  # ^ means not in a bracket
print(y)  # ['uct.ac.za']

# starts with From, space, any character, zero or more times, etc
y = re.findall('^From .*@([^ ]*)', text)
print(y)  # ['uct.ac.za']

# find spam confidence

hand = open('mbox.txt')
numlist = list()
for line in hand:
    line = line.strip()
    # starts with that string, extracts numbers and period, any number of times
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:  # gets rid of lines that have more than one numbers
        continue
    num = float(stuff[0])
    numlist.append(num)
# print(numlist)
print('Maximum', max(numlist))


x = 'We just received $10.00 for cookies'
# $ is a regex character (end of line) so if we want to find the normal character we add an escape character '\'
y = re.findall('\$[0-9.]+', x)
print(y)
