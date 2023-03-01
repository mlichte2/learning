# concatenating

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)
print(a)

# can be sliced

print(c[1:4])

# creating an empty list

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)

# does list contain value
print(99 in stuff)

# insert can insert a value into the list

stuff.insert(0, 'daves')
print(stuff)

names = ['kate', 'asad', 'jalo']

names.sort()
print(names)

# some addition

print(len(c))
print(max(c))
print(min(c))
print(sum(c))
print(sum(c)/len(c))

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average', average)

# technically the above is more memory effiecient since it uses one variable, a list, rather than two (total & count)
