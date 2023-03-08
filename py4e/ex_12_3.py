# unicode characters and strings

# ASCII is pretty old school -- like 1980s

print(ord('H'))  # ord() gives the numeric value of a simle ASCII character
print(ord('e'))

# in ASCII 1 character == 1 byte

# unicode is universal code -- has a shit load of characters
# multi-byte characters

# utf-16
# utf-32
# utf-8, recommended practice for encoding data to be exchanged between systems

# utf-8 works best when sending info between systems (say US -> JAP)

# python2 used both strings and unicode
# python3 uses unicode for everything

# python2 uses type string for bytes
# python3 uses class bytes for bytes

# python3 and unicode
# in python3 all strings are unicode
# working with string variables in python programs and reading data from files usually "just works"
# when we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to utf-8)

x = b"abc"
print(type(x))  # <class 'bytes'>

x = x.decode()  # defaults to utf-8, so normally just works
print(type(x))

x = x.encode()
print(type(x))

# your program
# 1: socket
# 2: connect
# 3: receive
# 4: recv

# encode to send
# decode once received
