zot = "banana"
print(zot[0])

print(len(zot))

print(zot[len(zot) - 1])


index = 0
while index < len(zot):
    letter = zot[index]
    print(index, letter)
    index += 1

for letter in zot:
    print(letter)

# the for loop is a bit more elegant
# the while loop can be more flexible
# in this case the for loop is better

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)

# slicing strings

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

# end is "up to but not including"
# if the second number is beyond the end of the string it stops at the end

print(s[:2])
print(s[8:])
print(s[:])
