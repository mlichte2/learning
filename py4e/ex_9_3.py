# dictionaries and files

string = '''the clown ran after the the car and the car ran into the tent and the 
tent fell down on the clown and the car'''

counts = dict()

words = string.split()
print(f"Words: {words}")

print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# definite loops and dictionaries

random = {
    'chuck': 1,
    'fred': 42,
    'jan': 100
}

for key in random:
    print(key, random[key])

# retrieving keys and values

print(random.keys())
print(random.values())
print(random.items())  # returns tuples

for aaa, bbb in random.items():
    print(aaa, bbb)
