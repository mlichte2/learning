# Lists

# Collections contain many values in a single "variable"

#

friends = ['Joseph', 'Mike', 'Dave']

# list element can be any python object even another list

numbers = [1, [2, 3], 4]

print(numbers[1][0])  # returns 2

# strings are immutable -- we cannot change the contents of a string -- we must make a new string to make any change
# lists are mutable -- we can change an element of a list using the index operater

lotto = [2, 14, 26, 41, 63]
lotto[2] = 28

print(lotto)

# how long is a list?

print(len(lotto))

# range function

print(range(4))

print(len(friends))

print(range(len(friends)))

for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year', friend)
