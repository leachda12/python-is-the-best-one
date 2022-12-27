# print("Hello World!")

# message = "hello python world!"
# print(message)
# print(message.title())
# print(message.upper())

# first_name = "psuedo"
# last_name = "intellectual"
# full_name = f"{first_name} {last_name}"
# # f-strings are used for concatenation
# print(full_name.title())
# message = f"I can't stand {full_name}s!"
# print(message)


# # lstrip removes left whitespace, rstrip removes right whitespace
# word = " python "
# print(word.lstrip())
# print(word.rstrip())
# print(word.lstrip().rstrip())
# # jk that one is easier
# print(word.strip)


# # use caps to indicate that a variable should be treated as a constant
# AH_YES = "that's nice"



# # ye olden zen of python
# import this



# # lists are lists
# names = ["abe", "gabe", "babe", "dabe"]
# # indexes and such
# print(names[3])
# # >> dabe
# # .append() to append, .insert() to insert at an index
# # .pop() to remove at an index, .remove() to remove the first with a specified value, .clear() to empty the list
# # .extend() to concatenate lists (or other iterables into a list)
# # .reverse() to flip the order of the list, .sort() to sort (a function can be used to specify the sorting)
# # can also use the del keyword to remove the value at a specified index
# # can also also sort without changing the list by using the sorted() function
# # .count() and the len() function can be used to tell the length
# # the index can be specified as two numbers separated by a colon (like [1:3]) to grab a specific range of values in a list
# # you can also leave the first number out ([:3]) if you want it to start from the start of the list
# # the same can be done for the second number ([1:]) if you want it to go to the end of the list
# # going negative with the first number ([-3:]) will grab starting from the end  
# # using the .copy() method or just the list name with a colon in the index brackets will create a copy of the list when used while defining a variable
# # like this: my_list = list[:]


# # tuples are immutable lists (they can't be changed)
# # instead of brackets, they use parentheses
# names = ("bob", "rob", "gob")
# # trying to change a value in a tuple will throw a type error
# # tuples can still be overwritten, it just won't keep the values



# # for loops 
# names = ["abe", "gabe", "babe", "dabe"]
# for name in names:
#   print(f"ah, {name}, what a perfect name")



# # range() for number ranges
# for num in range(1, 11): # one off
#     print(f"10 times {num} is {10 * num}")
# # lists of numbers can use the min(), max(), and sum() functions



# # good ol if statements
# # let's check for equalities
# # set the vartiable value
# fruit = "apple"
# # use double equals to test for equality
# fruit == "apple"
# # >> true
# fruit.upper() = "APPLE"
# # >> true

# #let's check for inequalities
# fav_number = 4
# # grab boolean for conditional
# fav_number <= 3
# # >> false
# fav_number > 4
# # >> false
# fav_number <= 4
# # >> true

# #multiple conditions
# age_1 = 28
# age_2 = 32
# age_1 >= 26 and age_2 < 32
# # >> false
# age_1 >= 22 and age_2 >= 32
# # >> true
# age_1 > 29 or age_2 > 29
# # >> true

# # checking inside lists
# fruits = ['bananas', 'apples', 'mangos', 'oranges']
# # use the in keyword
# 'apples' in fruits
# # >> true
# 'berries' in fruits
# # >> false

# # this time, using an if statement
# fruits = ['bananas', 'apples', 'mangos', 'oranges']
# fav_fruit = 'grapes'

# if fav_fruit not in fruits:
#     print(f"{fav_fruit} aren't in here")
# # >> grapes aren't in here


# if statement syntax
# if conditional_test:
    # do something

# if else syntax
# if conditional_test:
#     do something
# else:
#     do something else

# if elif else syntax
# if conditional_test:
#     do something
# elif other_conditional_test:
#     do another something
# else:
#     do the last something


# tips/tricks
# # using multiple if statements in a row is kosher
# fruits = ['bananas', 'apples', 'mangos', 'oranges']

# if 'bananas' in fruits:
#       print("Bananas are in")
# if 'berries' in fruits:
#     print("Berries are in")
# if 'mangos' in fruits:
#     print("Mangos are in")


# #use for loops for checking in lists
# fruits = ['bananas', 'apples', 'mangos', 'oranges']

# for fruit in fruits:
#     if fruit == "oranges":
#         print("oranges aren't actually in")
#     else:
#         print(f"{fruit} is in")


# # nested loops to check for value
# fruits = ['bananas', 'apples', 'mangos', 'oranges']

# if fruits:
#     print(f"{fruit} is in")
# else:
#     print("no fruits?")