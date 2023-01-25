# more variables and printing
# we will use a format string to insert variables into strings
# this uses curly braces {}
# string must be started with f
# print(f"{variable}")

name = "Michael Lichtenberger"
age = 28
height = 74  # inche
weight = 200  # lbs
eyes = 'hazel'
teeth = 'white'
hair = 'brown'

height_cm = round(height * 2.54, 1)
weight_kg = round(weight / 2.205, 1)

print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy.")
print("Actually thats not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(f"His weight in kg is {weight_kg} and height in cm is {height_cm}.")
