xfile = open('mbox-short.txt')

# for line in xfile:
#     print(line)

# count = 0
# for line in xfile:
#     count = count + 1
# print('Line Count: ', count)


inp = xfile.read()
print(len(inp))
print(inp[:20])

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue  # skips a line by conditional statement
    print(line)

for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.az' in line:
        continue  # skips a line by conditional statement
    print(line)

filename = input("Enter the file name: ")
try:
    filename = open(filename)
except:
    print('File cannot be opened:', filename)
    quit()
count = 0
for line in filename:
    if line.startswith('Subject:'):
        count += 1
print('There were ', count, 'subject lines in ', filename.name)
