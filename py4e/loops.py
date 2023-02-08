x = 5

while x > 0:
    print(x)
    x = x - 1

for i in [1, 2, 3, 4, 5]:  # called  a list in python
    print(i)

friends = ["asad", "jalo", "kate"]

for friend in friends:
    print(friend)

# finding the largest value 5.3

largest_so_far = -1
print('before', largest_so_far)
for item in [9, 41, 12, 3, 74, 15]:
    if item > largest_so_far:
        largest_so_far = item
    print(largest_so_far, item)

print('after', largest_so_far)

# loop idioms 5.4

zork = 0

print('before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('after', zork)

# summing the loop

print('before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('after', zork)

# finding the average

count = 0
sum = 0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum / count)

# filtering

print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('greater than 20', value)
print('after')

# search using a boolean

found = False
print('before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('after', found)

# finding smallest value

smallest = None  # flag value -- absenence of a value
print('before', smallest)
for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = the_num
    elif the_num < smallest:
        smallest = the_num
    print(smallest, the_num)
print('after', smallest)

# is and is not python has an is operatior that can be used in logical expressions
# implies "is the same as"
# similiar to, but stronger than ==
# is not, is also a logical operator
