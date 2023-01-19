# more printing...

# printing string
print("Mary had a little lamb.")
# printing f-string with snow added
# if you add a f before the "string" (f"""), it will error out because
# .format() does the same thing

print("Its fleece was white as {}.".format('snow'))
print("And everyhwere that Mary went.")

# prints the same string multiple times
print("." * 10)

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# print("",end(" ")) is a parameter to end the print statement with
# that string rather than a newline \n
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')


print(end7 + end8 + end9 + end10 + end11 + end12)
