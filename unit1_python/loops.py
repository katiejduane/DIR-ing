# ======================================== FOR LOOPS =============================================

# for loops iterate over a collection of items or through a range of numbers

# #syntax:
# for item in iterable_object:
#     #do something with item!

# #for loop with string
# for char in "hello":
#     print(char)

# for letter in "coffee":
#     print(letter*10)

# # a RANGE is a way of quickly generating numbers (within a specific range)
# for number in range(1,8):
#     print(number)
#     print(number*number)

# ranges in depth
# python ranges come in multiple forms:
range(7) #gives you integers from 0-6
range(1,8) #gives you integers 1-7
# if there is a third number, it's known as the step or interval
range(1,10,2) #gives you odds from 1-10
range(7, 0, -1) #gives you integers from 7 to 1

r = range(10)
list(r)
# print(list(r))

nums = range(1,10,2)
# print(list(nums))

# add up all the ODD numbers between 10 and 20
x = 0
for n in range(10, 21):  # remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n

# OR
for i in range(11, 21, 2):
        x += i

# # repeater exercise!
# times = input('how many times do i have to tell you!? ')
# times = int(times)

# for time in range(times):
#     # print('CLEAN UP YOUR ROOM!')
#     print(f"time {time}: CLEAN UP YOUR ROOM!")

# unlucky number exercise
# for 4 and 13, print 'x is unlucky', for even nums, print 'x is even', for odds, print 'x is odd'.
# for i in range(1, 21):
#     if i == 4 or i == 13:
#         print(f"{i} is unlucky!")
#     elif i % 2 == 0:
#         print(f"{i} is even!")
#     elif i % 2 != 0:
#         print(f"{i} is odd!")


# ======================================== WHILE LOOPS ===========================================
# there's a lot of things you can do with  a while loop that you can't do with a for loop!
# while loops execute while a certain condition is truthy and they end with they become falsy!
# they require more set up because they often rely on existing variable and a means to ensure
# the termination conditions WILL stop the loop, or else the loop will continue forever!

# im_tired = True

# while im_tired:
#     # seek caffeiene

# user_response = None
# while user_response != 'please':
#     user_response = input("ah ah ah, you didn't say the magic word! ")

# msg = input('what is the secret password? ')
# while msg != 'bananas':
#     print('wrong password, try again! ')
#     msg = input('what is the secret password? ')
# print('correct!')

# for num in range(1, 11):
#     print(num)

# VERSUS

# num = 1
# while num < 11:
#     print(num)
#     num += 2

# EMOJI EXERCISE!
# "\U0001f600" (code for specific emoji)

# for i in range(1, 11):
#     print("\U0001f600 "  * i) 

# x = 0
# while x < 11:
#     print("\U0001f600 " * x)
#     x += 1

# # nested option (a GROSS, GROSS solution according to mr. steele)
# for num in range(1, 11):
#     count = 1
#     smileys = ""
#     while count < num:
#         smileys += "\U0001f600 "
#         count += 1
#     print(smileys)

# # STOP COPYING ME exercise
# msg = input("Say Something: ")

# while msg != "stop copying me":
# 	print(msg)
# 	msg = input()
# print("UGH FINE YOU WIN, BROTHER!")

# BREAK keyword for EXITING our loops!
# while True:
#     command = input("Type 'exit' to exit: ")
#     if (command == "exit"):
#         break

# for x in range(1, 101):
#     print(x)
#     if x == 3:
#         break

# times = int(input("How many times do I have to tell you? "))

# for time in range(times):
# 	print("CLEAN UP YOUR ROOM!")
# 	if time >= 3:
# 		print("do you even listen anymore?")
# 		break

####################################### class practice ########################################
# # print a square
# width_count = 1
# while width_count < 5:
#     print(' *' * 5)
#     width_count += 1

# # coin counter
# coins = -1
# answer = 'yes'
# while answer == 'yes':
#     coins += 1
#     print('you have %d coins' % coins)
#     answer = input('do you want another? ')
# print('bye!')

# # centered triangle v1
# triangleHeight = 4
# count = 0
# stars = '*'

# while count < triangleHeight:
#     spaces = triangleHeight - count
#     print(' ' * spaces + stars)
#     count += 1
#     stars += '**'

# # centered triangle v2
# triangleHt = int(input('enter a number less than 14: '))
# count = 0
# stars = '*'

# while count < triangleHt:
#     spaces = triangleHt - count
#     print(' ' * spaces + stars)
#     count += 1
#     stars += '**'


# # The general approach to the Caesar Cipher problem:
# # For each letter in our message, look up the index in the alphabet (represented by a string).
# # Then, add 13 to that index.
# # If the value is greater than or equal to 26, then subtract 26 (to start over at 'a').

# encoded_message = "lbh zhfg hayrnea jung lbh unir yrnearq"
# # encoded_message = input("enter the messge here: ")

# # We will use a string that contains the alphabet.
# # This lets us use the `in` operator to see if a character in our message is a letter.
# # Also, we can ask for the `.index` of a letter.
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# rotate_by = 13  # We're doing ROT 13

# # Create a variable with an empty string that we'll add decoded letters to.
# decoded_message = ""

# # Iterate through the characters in our message.
# i = 0
# while i < len(encoded_message):
#     letter = encoded_message[i]
#     i = i + 1
#     # Anything that's not in the alphabet, just pass through to the decoded_message.
#     if letter not in alphabet:
#         decoded_message = decoded_message + letter
#     else:
#         # Grab the index in the alphabet.
#         index_in_alphabet = alphabet.index(letter)

#         # Add 13 (or whatever the amount of rotation is.)
#         new_index = index_in_alphabet + rotate_by

#         # See if we've exceeded the length of the alphabet.
#         if new_index >= len(alphabet):

#             # Shift back to the beginning of the alphabet, if necessary.
#             new_index = new_index - len(alphabet)

#         # Add the rotated letter to decoded_message..

#         decoded_message = decoded_message + alphabet[new_index]

# print(decoded_message)
