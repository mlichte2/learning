# parameters, unpacking, variables

from sys import argv


# read WYSS section for how to run this
script, first, second = argv
# argv == argument variable
# allows user to input from command line

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)

x = first
y = second
z = input("enter a third variable: ")


print(x, y, z)
