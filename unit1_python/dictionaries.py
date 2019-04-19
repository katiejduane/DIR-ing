# DICTIONARIES!!!!!!!!!!!

# dictionaries use KEY VALUE pairs to store data, they are
# NOT ordered! you create one by setting: dict_name = {}

cat = {"name": "Purrball", "age": 3.5, "is_cute": True, "color": "black"}

# you can also create a dictionary with the dict function
another_cat = dict(name='Luna', age=2)
# print(another_cat)

# accessing data in dictionaries!
weather = dict(cloudy=True, temp=72, wind_speed='13mph',
               humidity='57%', sunny=False, raining="on and off")
print(weather)

print(weather["cloudy"])  # we need quotes here because it is a string
# print(weather.temp)

artist = {
    "first": "Neil",
    "last": "Young",
}

# full_name = artist["first"] + " " + artist["last"]
# full_name = "{} {}".format(artist["first"], artist["last"])
full_name = f"{artist['first']} {artist['last']}"


# ITERATING OVER DICTIONARIES!
# a list on its own is already iterable, but a dictionary isn't

# accessing all values in a dict
# use .values()
for value in weather.values():
    print(value)

print(cat.values())

# we can also use .keys() to get the keys!
for key in weather.keys():
    print(key)

print(cat.keys())

# accessing both keys and values! --> use .items()
for item in weather.items():
    print(item)

print(cat.items())

for k, v in weather.items():
    print(f"key is {k} and value is {v}")

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)

total = 0
for val in donations.values():
    total += val

# print(total)

# using 'in' with dictionaries: does a dictionary have a key or a value?
print("humidity" in weather)
print("tornado" in weather)
print("Purrball" in cat.values())
print("tabby" in cat.values())
