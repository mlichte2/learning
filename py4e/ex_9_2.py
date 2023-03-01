# counting with dictionaries

# going to try and find the most common word

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)


count = dict()
for name in names:
    count[name] = count.get(name, 0) + 1
print(count)
