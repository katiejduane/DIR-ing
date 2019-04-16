# =================================== BOOLEAN AND CONDITIONAL LOGIC ===============================

# getting user input!
# name = input("enter your name: ")
# print("hi " + name)

# or

# print("what's your favorite color?")
# color = input() # doing it like this just allows the prompt to be entered beneath the prompt
# print("you said " + color)

# BOOLEAN EXPRESSIONS

# conditional statements
print ("What's your name, child?")
name = input()
if name == "katie":
    print("katie, your excellencey!")
elif name == "colt":
    print("how on earth!?")
else:
    print("how tragic your name isn't 'katie'")

# a worth on truthiness! and falsiness
x = 1
# x is 1 # True
# x is 2  # False
# but all values, not expressions, have inherent 'truthiness' or 'falsiness'
# Falsy: empty strings, empty objects, None, 0, False
# Truthy: strings, objects, 1, True

# Comparison operators!
# == truthy if a has same value as b
# =! truthy if a does NOT have same value as b
# < truthy if a is less than b
# > truthy is a is greater than b
# <= truthy if a is less than or equal to b
# >= truthy if a is greater than or equal to b

# Logical AND & OR
# and truthy if a AND be are true
if name == 'katie' and 'age' == 35:
    print('you are me')
# or truthy if a OR be are true
if name == 'katie' or 'age' == 35:
    print('we share something in common')
# not truthy if the opposite of a is true
weekend = False
if not weekend:
    print('go to work')

# == vs 'is'
# in python, 'is' and == are very similar
# == compares values
# is compares where it's stored in memory


# bouncer.py
age = input("How old are you: ")
if age:
	age = int(age)
	if age >= 18 and age < 21:
		print("You can enter, but need a wristband!")
	elif age >= 21:
	    print("You are good to enter and can drink!")
	else:
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")

# VERSION 2 with slightly refactored conditional logic
age = input("How old are you: ")
if age:
	age = int(age)
	if age >= 21:
	    print("You are good to enter and can drink!")
	elif age >= 18:
	    print("You can enter, but need a wristband!")
	else:
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")
