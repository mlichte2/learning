# reading and writing files

# close: closes the file
# readline: reads just one line of the textfile
# truncate: empties the file. watch out if careful about the file
# write('stuff'): writes "stuff" to the file
# seek(0): moves the read/write location to the beginning of the file

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If we don't want that, hit CTRL-C (^C).")
print("If you want to do that, hit RETURN")

input("?")

print("Opening the file...")
# "w" - Write - will overwrite any existing content
target = open(filename, "w")

print("Truncating the file. Goodbye!")
# truncate is not necessary since we are opening the file with the "w" param
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file")

txt = f"""{line1}\n{line2}\n{line3}\n"""

target.write(txt)

print("And finally, we close it.")
target.close()


# study drill 2
# file_to_read = open(filename)
# print(file_to_read.read())
# file_to_read.close()
