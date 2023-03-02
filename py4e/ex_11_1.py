# regex

# key is instead of programing with lines you use characters

# ^ beginning of line
# $ end of line
# . matches any character
# \s matches whitespace
# \S matches any non-whitespace character
# * repeats a character zero or more times
# *? repeats a character zero or more times (non-greedy)
# + repeats a character one or more times
# +? repeats a character one or more times  (non-greedy)
# [aeiou] matches a single character in the listed set
# [^XYZ] matches a single character not in the listed set
# [a-z0-9] the set of characters can includ a range
# ( indicates where the string extraction is to start
# ) indicates where the string extraction is to end

# must import

import re

# re.search()  # find-ish

# re.findall()  # extraction

# using like find
hand = open(('mbox.txt'))
# for line in hand:
#     line = line.strip()
#     if re.search('From:', line):
#         print(line)

# using like startswith

# for line in hand:
#     line = line.strip()
#     if re.search('^From:', line):  # carrot indicates we want it to be the first character of a line
#         print(line)

# wild card characters

# starts with, capital X, any character, 0 or more times, followed by a colon
wildcardregex = '^X.*:'

# for line in hand:
#     line = line.strip()
#     if re.search(wildcardregex, line):
#         print(line)

# will return X-Content-Type-Message-Body: text/plain; charset=UTF-8 & X-DSPAM-Result: Innocent, etc

# maybe we want more specific since we could pick up ones that have spaces

# starts with, captial X, dash character, any non-whitespace character (\S), one or more times, ending with a colon
betterregex = '^X-\S+:'

for line in hand:
    line = line.strip()
    if re.search(betterregex, line):
        print(line)
