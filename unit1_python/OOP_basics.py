# Define OOP, understand encapsulation and abstraction, create classes and instances
# and attach methods/properties to each!

# OOP: using code to represent or recreate things that exist in the world (a car, a user, a card,
# etc...) but not in code! it uses classes and objects to do this!

# CLASS: blueprints (recipes) for objets. they contain methods (functions) and attributes
# (similar to keys in a dictionary)

# OBJECT: an "instance" of a class. they contain their class's methods and properties.

# Encapsulation: the goal with OOP is the ecnapsulate our code into a logical hierarchical
# groupings using classes. The goruping of public and private attributes and methods into a
# programmatic class, making abstraction possible. Think of it as a little bubble; we want
# the fewest entries and exits into and out of that bubble as possible

# Abstraction: Exposing only the relevant data in a class interface, hiding private attibutes
# and methods (aka the 'inner workings') from users; simple hiding the complex. We abstract it!


# CREATING classes and intances! ----------------------------------------------->

# class naming: upper case first letter, but then camel case to follow, in the singular!
# class User:
#     # python will always look for the INIT method whenever we make a new class!
#     def __init__(self, first, last, age):
#         # self has to go there! it refers to each individual instance of a class!
#         # it must be the first paramater to not only __init__ but to any methods and
#         # properties on class instances!
#         self.first = first
#         self.last = last
#         self.age = age
#         self.__secret = "i like turtles!"

# #creating an objectthat is an instance of a class is called INSTANTIATING a class
# user1 = User('Bianca', 'LaBonita', 37)
# print(user1.first, user1.last)

# dunder methods, name mangling, and more! ----------------------------------------------->
# __name__ (two underscores before and after)
# these are special methods in python, don't go out and make your own dunder methods!

# __twoUnderscores: this actually does something behind the scenes (unlike _oneUnderScore).
# python is "mangling" the name that comes after two underscores. In order to access the data
# when something is named like this, you must do: print(user1_User__secret). Itmakes it PARTICULAR
# to this class, not necessarily to anything that inherits from this class.

# Adding Instance Methods! ----------------------------------------------->
# Special functions for each instance of a class! This is what really separates objects from dicts.

# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.__secret = "i like turtles!"

# # what would we actually put in a method? it depends on the class and what it needs to do.
#     def full_name(self):
#         # still need to provide self (first param)! because it references every unique instance of a class
#         return f"{self.first} {self.last}"
#     def initials(self):
#         return f"{self.first[0]}.{self.last[0]}."
#     def likes(self, thing):
#         return f"{self.first} likes {thing}."
#     def is_senior(self):
#         return self.age >= 65
#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th birthday, {self.first}!"

# user1 = User('Bianca', 'LaBonita', 37)
# print(user1.full_name())
# print(user1.initials())
# print(user1.likes('lizards'))
# print(user1.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)

# Classes/objects aren't just storage places for data (like dicts), they also have functionality!

# Introducing class attributes! ----------------------------------------------->
# class attributes are defined ONCE, and live on the class itself. They are shared by all instances
# of that class in the various objects made from it! They're less common than instance attributes

# class User:
#     active_users = 0 # this is a class attribute!
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.__secret = "i like turtles!"
#         User.active_users += 1
#         # anytime a new user is created, __init__ runs and this line adds another active user!

#     def logout(self):
#         User.active_users -= 1
#         # this instance method decrements the class attribute active_users ANYTIME a user logs out!
#         return f"{self.first} has logged out."

#     def full_name(self):
#         return f"{self.first} {self.last}"
#     def initials(self):
#         return f"{self.first[0]}.{self.last[0]}."
#     def likes(self, thing):
#         return f"{self.first} likes {thing}."
#     def is_senior(self):
#         return self.age >= 65
#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th birthday, {self.first}!"


# print(User.active_users) # note i am referring to the class itself and not an instance of it!
# print(User.active_users)

class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
# tony = Pet("Tony", "tiger") #throws an error

Pet.allowed.append('pig')  # adds to class attribute list
print(Pet.allowed)

# Class methods ------------------------------------>
# these are pretty rare, instance methods are far more common!
# but we still need to know how to write and recognize them
# they are not concerned with individual instances, but the class itself.


class User:
    active_users = 0

    @classmethod  # decorator for calling a class method
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    @classmethod  # decorator for calling a class method
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.__secret = "i like turtles!"
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}."

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}!"


user1 = User('Bianca', 'LaBonita', 37)
user1 = User('Bob', 'Buff', 76)

# calling the class method
print(User.display_active_users())

tom = User.from_string("Tom,Jones,54")
print(tom.full_name())


# the __repr__ method ------------------------------------>
# this method is one of several ways to provide a nicer string representation!

# see User class above for example of __repr__ method!
print(tom)



####### OOP part two! --------------------------------------->

# Inheritance!
# A key feature of OOP is the ability to define a class which
# inherits from another class (aka a 'parent' class)

# In python, inheritance works by apssing the parent class as
# an argument to the definition of a child class

# class Animal:
#     cool = True
#     def make_sound(self,sound):
#         print(f"this animal says {sound}")

# class Cat(Animal):
#     pass

# blue = Cat()
# blue.make_sound('meeeoooowwww')

# All about PROPERTIES! ---------------------------------->


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property  # decorator for property
    # above is syntax for a 'getter'
    def age(self):
        return self._age
        # this method allows you to print just 'jane.age'

    @age.setter
    # above is the syntax for a 'setter'
    def age(self, value):
            if value >= 0:
                self._age = value
            else:
                raise ValueError("age can't be negative!")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


jane = Human("jane", "goodall", 70)
# print(jane.get_age())
# jane.set_age(55)
# print(jane.get_age())
# print(jane.age)
# jane.age = 45
# print(jane.age)
# print(jane.full_name)


# Introduction to SUPER() ---------------------------------->

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super() .__init__(name, species="cat")
        # this refers to the PARENT CLASS (in this case, Animal)
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat('blue', 'scottish fold', 'string')
blue.make_sound('meeeoooowwww')

print(blue.toy)
blue.play()
print(blue)
