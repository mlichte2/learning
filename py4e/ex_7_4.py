fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        intstartsat = line.find(":")
        stringnum = line[intstartsat + 2:]
        num = float(stringnum)
        count += 1
        total += num
print("Average spam confidence:", total / count)
