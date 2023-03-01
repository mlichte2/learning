# Write a program to read through the mbox-short.txt and figure out who has sent the
# greatest number of mail messages. The program looks for 'From ' lines and takes the second
# word of those lines as the person who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a counts of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop
# to find the most prolific committer.


fname = input("Enter file: ")

if len(fname) < 1:
    fname = 'mbox.txt'

fh = open(fname)

counts = dict()

bigcount = None
bigword = None

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender, 0) + 1


for sender, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = sender

print(bigword, bigcount)
