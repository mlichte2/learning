# What was that?

# This \ (backslash) character encodes difficult-to-type characters into a string
# An important escape sequence is to escape a single-quote (') or double-quote
# ("). Imagine you have a string that uses double-quotes and you want to put a
# double-quote inside the string. If you write "I "understand" joe." then
# Python will get confused because it will think the double-quotes around
# "understand" actually ends the string. You need a way to tell Python that
# the double-quote inside the string isn’t a real double-quote.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# backslash things are called escape sequences in python

name = "Michael"
age = 25
lives_in = "Chicago"

person_info = """
{}'s info:\n
\tage = {}
\tlocation = {}
"""

print(person_info.format(name, age, lives_in))
