# input vars strings and type conversion
#
# strings
# course='python for beginners'
#        0123
# print(course[0])
# prints "p"
# print(course[-1])
# prints "s"
# print(course[0:3])
# prints"pyt"
# print(course[0:])
# prints "python for beginners"
# print(course[1:])
# prints "ython for beginners"
# print(course[:])
# prints "python for beginners"
#
#
#
# input/typeconvertion/strings/vars
# by= input ('birth year: ')
# age = 2022 - int(by)
# print(age)
# print(type(age))
#
#
# string methods
# hello="bonjuer"
# print(len(hello))
# print(hello.upper)
# real method
# put name of exsisting var
# ex: hello.#####
# put a dot then you get prompts
# hello.upper
# hello.find("bon")
#
# arithimitec operations
#
#   exponent ** - x ** y = x to the power of y
#   divide /(float) //(int) %(remainder)
#   add +
#   subtract -
#   multiply *
#
# math functions
# https://docs.python.org/3/library/math.html
#
#
# IF STATMENTS
# if is_hot:
#  print(“hot day”)
# elif is_cold:
#  print(“cold day”)
# else:
#  print(“beautiful day”)
#
#
# Logical operators:
# price=1111111
# has_good_credit=true
# if has_high_income and has_good_credit:
#   down_payment = 0.1 * price
# else:
#   down_payment = 0.2 * price
# print(f"down payment: ${down_payment}")
#
#
# is_day = True
# is_night = not is_day
#
#
# logical operatrios
#
# and=both,or=at least one,not reverses boolian "true""false"
#
# and not
#
#
# has_high_income = False
# has_good_credit = True

# if has_high_income and has_good_credit:
#   print("hallal loan okayzz")
# else:
#     print("NOT HALLAL LA ILLAHA ILA ALLAH")
#
#
# comparison operatirs
#
# > greater   < less  >= greater equal   <= less equal  == equal  != Not Equal
#
# temp=30
#
# if temp >= 30:
#     print("Game'Last One Standing'  Me'Oh God' Sun >:-) ")
# else:
#     print("hello soviets from snobiden")
#
#
#
#
#
# wight conversin program
#
# weight = input("Insert Weight: ")
# unit = input("Did You Insert Your Weight In (L)bs Or (K)g: ")

# if unit.upper() == "L":
#     converted=int(weight) * 0.45
#     print (f"You Are {converted} In Kilos")
# else:
#     converted = int(weight) / 0.45
#     print (converted)
#
# while loops
#
# i = 0
# while i <= 5:
#     print("*"*i)
#     i = i + 1
# print("done")
#
#
# from ast import Break
# secret = 666
# guess_count = 0
# guess_limit = 2
# while guess_count <= guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret:
#         print("Let's GOOOOOOOOO So Spooky")
#         break
# else:
#     print(f"Broo Is Trash at THe THree Am CHALLEnge 100% Real !!!!111!!1!!!")
#     Break
#
# Car Game Go BROOOOOOOM
#
#for loops
#
#for item in "python":
#   print(item)
#for intel in ["mosh", "dosh", "gosh"]
#   print (intel)
#
#
# for inte in range(1001):
#     print (inte)
#
# prices = [10,20,30,500,1999999999999]
# total = 0
# for price in prices:
#     total += price
#     print (f"total: {total}")
#
#nested loops
#
#(x, y)
#(0, 0)
#
# for x in range(4):
#     print(" X, Y")
#     for y in range(3):
#         print(f"({x}, {y})")
# 
# lists
# names = ["jhon", "elchacho", "mobie"]
# #          0          1         2
# print (names)
# print(names[2:])
# 
# 
# 
# 
# 
# 
# 
# 
# indexes
# bar= ["jhon", "elchacho", "mobie"]
# print(bar[2:])
# 
# 2d listes
# 
# matrix =[
#     [1, 2 , 3],
#     [4, 5, 6,],
#     [7, 8, 9,]
# ]
# matrix[0][1]=20
# print(matrix[0][1])
# 
# for row in matrix:
#     for item in row:
#         print(item)
# 
# list methods
# 
# numbers = [5, 2, 1, 7, 4]
# numbers.insert(0, 10.)
# print(50 in numbers)
# print(numbers)
# 
# 
# tuples
# numbers = (1,2,3)
# unchangable stuff
# 
# unpacking

cord = (1,2,3)
# X = cord[0]
# y = cord[1]
# z = cord[2] 
# x, y, z = cord
# print (y)
# 
# doctinary
# 
# customer = {
#     "name": "john smith",
#     "age": 30,
#     "isgood": True
# }
# customer["name"] = "jack smith" #add stuff name and  info
# print(customer[name]) #print stuff
# print(customer.get("birthdate", "Jan 1 1980")) #print default

# 
# functions
# 
# def imposter(bats):
#     print ("amogus sus")
#     print (bats)
#     return
# imposter(impos = "am")
# 
# exeptions
# try:
#     age = int(input("Age: "))
#     print (age)
# except ValueError:
#     print ("STobid")

# 
# 
# 
# 
# 
# 
# classes
# 
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")
# point = Point(10, 20)
# print(point.x)

# construcktors
# 
# def __init__(self, x, y):
#         self.x = x
#         self.y = y
# 
# 
# 
# inheritance
# class Animal:
#     def walk(self):
#         print("walk")


# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass
# 
# MOdules
# import convers

# convers.died(300)
# 
# packedges
#   from import
# 
# gen rand val
# 
# import random
# for i in range (999):
#     print (random.randint(20,30))
#     random.random()
#     print ()

# membs = ["hamza", "joe", "elbozo"]
# boss = random.choice(membs)
# print (boss)
# 
# working with directories
# 
# from pathlib import Path

# path = Path()
# for file in path.glob("*"):
#     print(file)
# print(path.exists())
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
