from characters import characters

print(len(characters))
jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# for k in jon_snow:
#     print(k)

# # print out just the values
# for k in jon_snow:
#     print(jon_snow[k])

# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))

# def get_k():
#     k_names = []
#     for k in characters:
#         if k["name"][0] == "K":
#             k_names.append(k["name"])
#     print(len(k_names))
#     return k_names
            

# print(get_k())

# def get_names():
#     a_names = []
#     for char in characters:
#         first_initial = char["name"][0]
#         if first_initial == "A":
#             a_names.append(char["name"])
#     return a_names

# # print(get_names())


# names = ["Agrivane", "Alvyn Sharp", "Argrave the Defiant"]
# for name in names:
#     name_list = name.split(" ")
#     if len(name_list) > 1:
#         print(name_list[1])


nums = [1,2,5,8,3,9,7]
def get_biggest(list):
    biggest = 0
    for num in nums:
        if num > biggest:
            biggest = num
    return biggest

print(get_biggest(nums))
        

