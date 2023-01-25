# strings and text

# strings can be either single '' or double "" quotes
# f in print(f"Here is a {variable}"), is a special type of string to format.
# It is called an f-string
# there is also another kind of formatting using .format() syntax
# This allows you to apply a format to an already-created string such as in a loop

types_of_peoples = 10
x = f"There are {types_of_peoples} types of peoples."

binary = 'binary'

do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said '{y}'")

hilarious = False
joke_evalution = "Isn't that joke so funny! {}"

print(joke_evalution.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
