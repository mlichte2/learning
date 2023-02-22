# string concatination

a = 'string'
print(a + " " + "more string")

# using in as a logical operator

fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)

if 'a' in fruit:
    print('Found it!')

word = 'banana'

if word == 'banana':
    print('All right, bananas')

if word < 'banana':
    print(f"Your word, {word}, comes before banana")
elif word < 'banana':
    print(f"Your word, {word}, comes after banana")
else:
    print('All right, bananas')

greet = 'Hello Bob'
zap = greet.lower()

print(zap)
print(greet)

print('Hi there'.lower())
print('Hi there'.upper())

# .lower() is a method

stuff = 'Hello World'

print(type(stuff), "\n", dir(stuff))

# searching for a string
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)
# returns -1 when it cannot find

nstr = greet.replace('Bob', 'Jane')
print(nstr)

nstr = greet.replace('o', 'X')
print(nstr)

# stripping whitespace

greet = '         Hello Bob    '


print(f"""{greet.lstrip()}
{greet.rstrip()}
{greet.strip()}""")

# Prefixes

line = 'Please have a nice day'
print(line.startswith("P"))

# Parsing and Extracting

data = 'From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1: sppos]
print(host)

# python3 all characters are unicode
# in python2 there were two types of strings unicode and just strings

x = 'From marquard@uct.ac.za'
print(x.find("uct"))
print(x[14:17])
