
hrs = input("Enter hours:")
rt = input("Enter the hourly rate:")

try:
    h = float(hrs)
    r = float(rt)
except:
    print("error, please enter numeric input")
    quit()  # ends the program since the data does not make sense

if h <= 40:
    pay = h * r
    print(pay)
elif h > 40:
    ot_h = h - 40
    h = h - ot_h
    pay = (ot_h * (r * 1.5)) + (h * r)
    print(pay)
else:
    print("error")
