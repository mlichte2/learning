# Week 1

all langugages have reserved words
example if, else, global, from, etc

interation
while and for loops

# Week 4

- Constants
  fixed values, duh

- naming rules

must start with a letter or underscore
case sensitive

Mnemonic naming
choose a sensible variable name
ie instead of a and b; hours and rate

operators are the same as JS

order of evalution, if you want something to to take presedence just use parentheses
if you dont use parentheses P(), Power, M\*, A+/-,L->R

type() function tells you what type a variable is

numbers have two types

integers
-1, 23, 40000

float point numbers
-2.5, 0.0, 98.6
^ don't use float points with money

float() function turns int -> float

integer divistion produces a float point result

python 2 will not give remainders for two ints that divide
5/2 = 4
^fixed in python 3

str() converts number to sting

# week 5

- conditionals

if statement
if statement is true then it will run that command

== is the equality opperator in python: != is not equal

indentation is incredibly important in python

tabs can sometimes confuse tab and 4 spaces
there is a setting in vs code to change this
converttabstospaces and vice-versa

conditional vs sequencial code vs nested code

if / else

```
x = 4
if x > 2 :
	print('Bigger')
else:
	print('Smaller')
print('All done')
```

elif is part of the multiway conditionals
done in sequence

if and elif can be used without and else statement

```
if

elif

else
```

the try / except structure

a way to catch a traceback or error

```
astr = "hello bob"
try:
	istr= int(astr)
except:
	istr= -1 # this line would run
```
