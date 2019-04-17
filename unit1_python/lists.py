# ===================================== basic list syntax =========================================
my_fruit_list = ['banana', 'grape', 'cherry', 'pineapple']
my_mixed_list = [1, 13, 'aloha', 22.7, 'green']

# get list length with len()
print(len(my_fruit_list))

# you can declare a list with a variable = [] OR use the list()
tasks = list(range(1, 4))
print(tasks)

# ==================================== accessing data in lists... ===================================
# lists are ORDERED! like ranges, lists always start counting at zero! the first element ALWAYS
# lives at index 0!
my_fave_fruit = my_fruit_list[2]
print(my_fave_fruit)

# a neg number will index backwards!
print(my_fruit_list[-1])  # pineapple!

# check if a value is IN a list!
print('watermelon' in my_fruit_list)  # False
print('grape' in my_fruit_list)  # True

# fancier -->
if "cherry" in my_fruit_list:
    print("it's myfavorite fruit, too!")


# ====================================== ITERATING OVER LISTS! ===============================
# for fruit in my_fruit_list:
#     print(fruit)

# numbers = [4,6,2,4,8,9,7,10]
# for num in numbers:
#     print(num * num)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# index = 0
# while index < len(my_mixed_list):
#     print(my_mixed_list[index])
#     index += 1

# while index < len(my_fruit_list):
#     print(f"{index}: {my_fruit_list[index]}")
#     index += 1

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ''
for s in sounds:
    result += s.upper()

print(result)

# ========================================== LIST METHODS ==========================================

# append adds one item to the end of the list
my_fruit_list.append('papaya')
print(my_fruit_list)

# extend adds multiple items to the end of the list, but must be enclosed in square brackets []
my_mixed_list.extend([101, 'juicebox'])
print(my_mixed_list)

# insert inserts an item into a specific index in a list
# the first arg is the index you want to pass the date to! the second arg is what to add!
my_fruit_list.insert(2, 'passionfruit')
print(my_fruit_list)
# but it's inserted at second to last spot! so...
my_mixed_list.insert(-1, 'the end!')
my_mixed_list.insert(len(my_mixed_list), 'last')
print(my_mixed_list)

# clear removes all items from the list at once!
silly_list = [1, 2, 3, 4, 5, 1, 2, 3]
# silly_list.clear()
# print(silly_list)

# pop removes a single item at a particular index, or last item by default
# silly_list.pop()
# print(silly_list)
# silly_list.pop(1)
# print(silly_list)

# remove removes the item the matches the value provided; and ONLY the first value found!
# if it's not found, it'll throw an error
# silly_list.remove(2)
# print(silly_list)

# index
print(my_fruit_list.index('cherry'))
# can specify a starting point (second arg):
print(silly_list.index(1, 2))

# count
print(silly_list.count(1))

# # sort
# silly_list.sort()
# print(silly_list)

# # reverse
# silly_list.reverse()
# print(silly_list)

# join
words = ['coding', 'is', 'fun']
print(' '.join(words))

# ======================================== SLICING! ==========================================
# make new lists using slices of old list!
# syntax: some_list[start:end:step]
slice_off = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# print(slice_off[1:]) # slices off every thing after the 1st index because no end is provided!
# print(slice_off[3:]) # slices off every thing after the 3rd index because no end is provided!

# we can also use neg numbers to slice FROM the END of the list
# print(slice_off[-1:])
# print(slice_off[-3:])

# using the second arg: where to stop! (exclusive counting)
# print(slice_off[:3])
# print(slice_off[1:3])
# print(slice_off[1:-1])

# using the third arg: the step! (the number to count at a time)
# print(slice_off[1::2])
# print(slice_off[::2])
# print(slice_off[1:-1:2])
# a neg number will reverse the order!
print(slice_off[::-1])


# ================================ swapping values in lists! =================================

pals = ["emily", "ellen"]
pals[0], pals[1] = pals[1], pals[0]
print(pals)

# you might need to swap values when shuffling, sorting, algorithms in general
