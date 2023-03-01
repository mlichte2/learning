fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'mbox.txt'  # make sure to change this to mbox-short.txt before submitting

fh = open(fname)

emails = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        pieces = line.split()
        email = pieces[1]
        emails.append(email)

for email in emails:
    print(email)
print("There were", len(emails), "lines in the file with From as the first word")
