# Files

# gonna send some stuff to secondary memory

# opening the file

fhand = open('mbox-short.txt')
# fhand is a handle that is a reference to the location of the file
print(fhand)
# retunrs just info about the file
# <_io.TextIOWrapper name='mbox-short.txt' mode='r' encoding='UTF-8'>

print(fhand.read())
