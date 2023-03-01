# tuples
# they are like lists

# immutable

z = (5, 4, 3)
try:
    z[0] = 10
except:
    print('Not mutable')

t = tuple()
print(dir(t))

# more efficient and preformative because they cannot be changed

(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

# the items() method in dictionaries returns a list of (key, value) tuples

d = {
    'csev': 2,
    'caen': 4
}

for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)  # returns list of tuples

tups = sorted(tups)
print(tups)

d = {
    'a': 10,
    'b': 1,
    'c': 22
}

for k, v in sorted(d.items()):
    print(k, v)

# ^ loops through dictionary in key order

c = d

tmp = list()
for k, v in c.items():
    tmp.append((k, v))  # list of tuples again

print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

# ten most common words

fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


# can replace this whole thing with one line... see below

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)


lst = sorted(lst, reverse=True)
print(lst)

for val, key in lst[:10]:
    print(key, val)


# see here!
print(c)

print(sorted([(v, k) for k, v in c.items()], reverse=True))
# list comprehension creates a dynamic list. in this case, we make it a list of reversed tuples and
# then sort it
