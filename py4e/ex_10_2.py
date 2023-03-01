name = input("Enter file:")
if len(name) < 1:
    name = "mbox.txt"
handle = open(name)

times = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    else:
        line = line.split()
        time = line[5]
        time = time.split(":")
        hour = time[0]
        times[hour] = times.get(hour, 0) + 1

sorted_times = list()

for time, count in times.items():
    sorted_times.append((time, count))

sorted_times = sorted(sorted_times)


for t, c in sorted_times:
    print(t, c)
