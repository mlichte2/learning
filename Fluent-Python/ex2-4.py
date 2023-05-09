colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# arranged by color then size
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)


for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes  # arranged in size then color (just flip the for clause)
           for color in colors]

print(tshirts)
