# lists and strings

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

line = 'A lot'
etc = line.split()
print(etc)
line = "first;second;third"
thing = line.split()
print(thing)
thing = line.split(';')
print(thing)
print(len(thing))

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])  # gets day of the week

# double split pattern

string = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
email = string.split()
sender = email[1]
print(sender)

sender = sender.split('@')
print(sender)

sender_name = sender[0]
domain = sender[1]

print('Sender:', sender_name)
print('Domain:', domain)
