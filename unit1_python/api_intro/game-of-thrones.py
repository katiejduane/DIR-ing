from characters import characters
<<<<<<< HEAD
# print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}
=======

print(len(characters))
jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}
>>>>>>> bb26cf1bbc38406d0c8c3da7413b8f3898fdb6f5

# # print out the key names individually
# for k in jon_snow:
#     print(k)

# # print out just the values
# for k in jon_snow:
#     print(jon_snow[k])

# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))

<<<<<<< HEAD
# def all_names():
#     for n in characters:
#         print(n["name"])

# all_names()

# How many characters names start with "A"?
a_name_list = []
def a_names(a_name_list):
    for k in characters:
        if k["name"][0] == "A":
           a_name_list.append((k["name"]))
    return a_name_list

a_names(a_name_list)
print(len(a_name_list))

# How many characters names start with "Z"?
z_name_list = []
def z_names(z_name_list):
    for k in characters:
        if k["name"][0] == "Z":
           z_name_list.append((k["name"]))
    return z_name_list

z_names(z_name_list)
print(len(z_name_list))

# How many characters are dead?
dead_char = []
def dead_char_count(dead_char):
    for k in characters:
        if k["died"] != "":
            dead_char.append((k))

dead_char_count(dead_char)
print(len(dead_char))

# Who has the most titles?
def char_titles():
    title_count = 0
    name = ""
    for k in characters:
        if k["titles"] != [""] or k["titles"] != ['']:
            if len(k["titles"]) > title_count:
                title_count = len(k["titles"])
                name = k["name"]
    print(f"{name} has {title_count} titles, which is more than any other character")

char_titles()

# How many are Valyrian?

valyrian = []

def is_valyrian(valyrian):
    for k in characters:
        if k["culture"] == "Valyrian":
            valyrian.append((k))
    return len(valyrian)

print(is_valyrian(valyrian))

# What actor plays "Hot Pie" (and don't use IMDB)?

def hot_pie():
    for k in characters:
        if k["name"] == "Hot Pie":
            print(k["playedBy"])
hot_pie()

# How many characters are *not* in the tv show?

def book_char():
    not_on_show = []
    for k in characters:
        if k["tvSeries"] == [""] or k["tvSeries"] == ['']:
            not_on_show.append((k["name"]))
    return len(not_on_show)
print(book_char())

# Produce a list characters with the last name "Targaryen"


# Create a histogram of the houses (it's the "allegiances" key)
=======
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
        

>>>>>>> bb26cf1bbc38406d0c8c3da7413b8f3898fdb6f5
