# HTML AND CSS QUESTIONS: you MUST answer these! research/discuss in groups!

# 1.
# 2.
# 3.
# 4.
# 5.
# 6.


# Algorithms --------------------------------------------->

# 1) write a function that accepts a number and returns a list of of its factors, starting with 1 and going up to the number.
#     '''
# find_factors(10) # [1,2,5,10 ]
# find_factors(11) # [1,11]
# find_factors(111) # [1,3,37,111 ]
# find_factors(321421) # [1,293,1097,321421 ]
# # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
# find_factors(412146)
# '''

def find_factors():
    pass



# 2) Write a function that accepts 2 numbers and returns true if they have the same frequency of digits, and false if they do not.
#     '''
# same_frequency(551122,221515) # True
# same_frequency(321142,3212215) # False
# same_frequency(1212, 2211) # True
# '''

def same_frequency():
    pass



# 3) Write a function that accepts a list of numbers and returns true if any 3 consecutive numbers sum to an odd number, and false if they do not.
#     '''
# three_odd_numbers([1,2,3,4,5]) # True
# three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
# three_odd_numbers([5,2,1]) # False
# three_odd_numbers([1,2,3,3,2]) # False
# '''

def three_odd_numbers():
    pass



#############################################################

# Answers to Qs:


# Solutions:

# find_factors ------------------------------------------->

# def find_factors(num):
# factors=[]
# i=1
# while(i <= num):
# if (num % i == 0):
# factors.append(i)
# i += 1
# return factors

# same_frequency ---------------------------------------->

# def same_frequency(num1, num2):
# d1={letter: str(num1).count(letter) for letter in str(num1)}
# d2={letter: str(num2).count(letter) for letter in str(num2)}

# for key, val in d1.items():
# if not key in d2.keys():
#     return False
# elif d2[key] != d1[key]:
#     return False
# return True

# three_odd_numbers -------------------------------------->

# def three_odd_numbers(arr):
# i=0
# while(i < (len(arr) - 2)):
# total=0
# j=i
# while(j <= i+2):
# total += arr[j]
# j += 1

# if (j-i) % 3 == 0 and total % 2 != 0:
#     return True

# i += 1
# return False
