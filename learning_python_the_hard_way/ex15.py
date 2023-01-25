# reading files

# importing a module
from sys import argv

# setting up argument variables
script, filename = argv

# pydoc open for docs, just opens a file
txt = open(filename)

print(f"Here's your file {filename}:")

# read is a function that reads the file
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
