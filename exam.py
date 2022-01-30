# VARIABLES EP2
# -----------------------------------------------------------
# first_name = "Robin"
# last_name = "Stardust"
# full_name = first_name + " " + last_name
# print("Hello " + full_name)
# print(type(full_name))

# age = 16
# age += 1
# print("Your age is: " + str(age))
# print(type(age))

# height = 250.5
# print("Your height is: " + str(height) + "cm")
# print(type(height))

# human = False
# print("Are you a human:"+ str(human))
# print(type(human))
# -----------------------------------------------------------
# MULTIPLE ASSIGNMENT EP3
# -----------------------------------------------------------
# name = "Robin"
# age = 16
# attractive = True

# name, age, attractive, = "Robin", 16, True

# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)
# -----------------------------------------------------------
# STRING METHODS EP4
# -----------------------------------------------------------
# name = "Robin Stardust"

# print(len(name))
# print(name.find("S"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('t'))
# print(name.replace('t', 'q'))
# print(name*5)
# -----------------------------------------------------------
# TYPECAST EP5
# -----------------------------------------------------------
#type casting = convert the data type of a value to another data type

# x = 1 #int
# y = 2.0 #float
# z = "3" #str

# x = float(x)
# y = float(y)
# z = float(z)

# print(x)
# print(y)
# print(z*3)
# -----------------------------------------------------------
# HOW TO GET INPUT EP6
# -----------------------------------------------------------
# name = input("What is your name?: ")
# age = int(input("What is your age?: "))
# height = float(input("What is your height?: "))

# print("Your name is: " + name)
# print("Your age is: " + str(age))
# print("Your height is: " + str(height))
# -----------------------------------------------------------
# MATH MODULE EP7
# -----------------------------------------------------------
# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))
# -----------------------------------------------------------
# STRING SLICING EP8
# -----------------------------------------------------------
# slicing = create a substring by extracting elements from another substring
#                    indexing[] or slice()
#                    [start:stop:step]

# name = "Robin Stardust"
# first_name = name[:5]
# last_name = name[6:]
# funky_name = name[::2]
# reversed_name = name[::-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website = "https://google.com"
# website2 = "https://wikipedia.com"
# slice = slice(8,-4)
# print(website[slice])
# print(website2[slice])
# -----------------------------------------------------------
# IF STATEMENT EP9
# -----------------------------------------------------------
# if statement = a block of code that will execute if it's condition is true

# age = int(input("how old are you?: "))

# if age == 100:
#     print("You are a century old!")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")
# -----------------------------------------------------------
# LOGICAL OPERATORS EP10
# -----------------------------------------------------------
# logical operators (and, or, not) = used to check if two or more conditional statements is true
# temp = int(input("What is the temperature outside?: "))

# if temp >= 0 and temp <= 30:
#     print("the weather is good today!")
#     print("go outside!")
# elif not(temp >= 0 and temp <= 30):
#     print("the weather is bad today!")
#     print("stay inside!")
# -----------------------------------------------------------
# WHILE LOOPS EP11
# -----------------------------------------------------------
# while loop = a statement that will execute it's block of code, as long as it's condition remains true

# while 1 == 1:
#     print("Help! I'm stuck in a loop!")

# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello "+name)
# -----------------------------------------------------------
# FOR LOOPS EP12
# -----------------------------------------------------------
# for loop = a statement that will execute it's block of code a limited amount of times (while loop = unlimited, for loop = limited)

# for i in range(10):
#     print(i+1)

# for i in range(50,100+1):
#     print(i)

# for i in range(50, 100+1, 2):
#     print(i)

# for i in "Robin Stardust":
#     print(i)

# import time

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year")
# -----------------------------------------------------------
# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()
# -----------------------------------------------------------
# Loop Control Statements = change a loops execution from it's normal sequence

# break =   used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for i in range(10):
#     if i == '-':
#         continue
#     print(i, end="")

# for i in range(21):
#     if i == 13:
#         pass
#     else:
#         print(i)

# food = ["sushi", "hotdog", "spaghetti", "hamburger", "pizza"]
# for x in food:
#     print(x)

# ---------------------------------------------------------------
# tuple = collection which is ordered and unchangeable used to group together related data

# student = ("Bro", "Robin", "Troy")

# print(student.count("Troy"))
# print(student.index("Bro"))

# for x in student:
#    print(x)
# -----------------------------------------------------------
# Dictionary\
# -----------------------------------------------------------
# capitals = {'USA':'Washington DC',
#             'India': 'New Dehli',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}

# print(capitals['Turkey'])
# print(capitals.get('Turkey'))
# for key,value in capitals.items():
#     print(key, value)

# -----------------------------------------------------------
# index operator [] = gives access to a sequence's element (str, list, tuples)

# name = "robin Stardust"

# if(name[0].islower()):
#     name = name.capitalize()

# first_name = name[:5].upper()
# last_name = name[6:].lower()
# full_name = first_name + " " +  last_name

# print(full_name)
# -----------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------
# function = a block of code which is executed only when it is called.

# def hello(name, ag3):
#     print("Hello " + name)
#     print("You are " + ag3 + " years old!")
#     print("Have a nice day!")

# first_name = str(input("Please enter your first name: "))
# last_name = str(input("Please enter your last name: "))
# full_name = first_name + " " +last_name
# age = str(input("Please enter your age: "))

# hello(full_name, age)
# -----------------------------------------------------------
# Return Statements
# -----------------------------------------------------------
# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function's return

# def multiply(number1, number2):
#     return number1 * number2

# print(multiply(4,4))
# ------------------------------------------------------------
# Keyword Arguments
# ------------------------------------------------------------
# def hello(middle, last, first):
#     print("Hello "+first+" "+middle+" "+last)

# hello(first = "Robin", middle = "robinOP", last = "Stardust")

# ------------------------------------------------------------
# Nested Functions
# ------------------------------------------------------------
# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

# num = input("Enter a whole positive number.")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole number.")))))
# ------------------------------------------------------------
# *args (params)
# ------------------------------------------------------------
# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

# def add(*args):
#     sum = 0
#     args = list(args)
#     args[0] = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(1,2,3,4,5,6))
# -----------------------------------------------------------
# **kwargs
# -----------------------------------------------------------
# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword

# def hello(**kwargs):
#     # print("Hello " + name1 + " " + name2)
#     print("Hello ", end=" ")
#     for key,value in kwargs.items():
#         print(value, end=" ")

# hello(name1="Robin", middle="robinOP",name2="Stardust")
# -----------------------------------------------------------
# str.format() = optional method that gives users more control
#                when displaying output

# animal = "cow"
# item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item)) #positional argument
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument
# ------------------------------------------------------------
# try, except, else, finally blocks
# ------------------------------------------------------------
# exception = events detected during execution that interrupt the flow of a program

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denumerator = int(input("Enter a number to divide by: "))
#     result = numerator / denumerator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero! idiot!")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers please")
# except Exception as e:
#     print(e)
#     print("Something went wrong :(")
# else:
#     print(result)
# ------------------------------------------------------------
# working with files
# ------------------------------------------------------------
# import os

# path = "/home/robinop/projects/ah"

# if os.path.exists(path):
#     print("This location is exist!")
#     if os.path.isfile(path):
#         print("This is a file!")
#     elif os.path.isdir(path):
#         print("This is a directory!")
# else:
#     print("This location doesn't exist!")
# ------------------------------------------------------------
# read contents of file
# ------------------------------------------------------------
# try:
#     with open('example.py') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found :(")
# ------------------------------------------------------------
# writing files
# ------------------------------------------------------------
# text = "Yooooooooo\n This is some text\n Have a good one\n"
# with open('test.py', 'w') as file:
#     file.write(text)
# ------------------------------------------------------------
# copying files
# ------------------------------------------------------------
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

# import shutil
# shutil.copyfile('test.py', 'test2.py') #src,dst
# ------------------------------------------------------------
# move files
# ------------------------------------------------------------
# import os

# source = "example.py"
# destination = "/home/robinop/Downloads/example.py"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" was not found")
# ------------------------------------------------------------
# modules
# ------------------------------------------------------------
# import messages as msg

# msg.hello()
# msg.bye()
# ------------------------------------------------------------
# rock-paper-scissors game
# ------------------------------------------------------------
# import random

# while True:
#     choices = ["rock","paper","scissors"]

#     computer = random.choice(choices)
#     player = None

#     while player not in choices:
#         player = input("rock, paper, or scissors?: ").lower()

#     if player == computer:
#         print("computer: ",computer)
#         print("player: ",player)
#         print("Tie!")

#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     elif player == "scissors":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     play_again = input("Play again? (yes/no): ").lower()

#     if play_again != "yes":
#         break

# print("Bye!")
# -----------------------------------------------
# quiz game
# -----------------------------------------------
# def new_game():

#     guesses = []
#     correct_guesses = 0
#     question_num = 1

#     for key in questions:
#         print("-------------------------")
#         print(key)
#         for i in options[question_num - 1]:
#             print(i)
#         guess = input("Enter (A, B, C or D): ")
#         guess = guess.upper()
#         guesses.append(guess)

#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1

#     display_score(correct_guesses, guesses)

# def check_answer(answer, guess):

#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0

# def display_score(correct_guesses, guesses):
#     print("-------------------------")
#     print("RESULTS")
#     print("-------------------------")
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()

#     print("Guesses: ", end= "")
#     for i in guesses:
#         print(i, end=" ")
#     print()

#     score = int((correct_guesses/len(questions)) * 100)
#     print("Your score is: "+ str(score)+"%")

# def play_again():

#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()
#     if response == "YES":
#         return True
#     else:
#         return False

# questions = {
#     "Who created Python?: ": "A",
#     "What year was Python created?: ": "B",
#     "Python is tributed to which comedy group?: ": "C",
#     "Is the Earth Round?: ": "A"
# }

# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#           ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

# new_game()

# while play_again():
#     new_game()
# ---------------------------------------------------
# OBJECT ORIENTED PROGRAMMING WITH PYTHON (POP)
# ---------------------------------------------------
# from car import Car

# car_1 = Car("Chevy", "Corvette", 2022, "Blue")
# car_2 = Car("Ford", "Mustang", 2022, "Red")

# car_2.drive()
# car_2.stop()
# ---------------------------------------------------
# class Car:
#     color = None

# class Motorcycle:
#     color = None

# def change_color(vehicle, color):
#     vehicle.color = color

# car_1 = Car()
# car_2 = Car()
# car_3 = Car()

# bike_1 = Motorcycle()
# bike_2 = Motorcycle()
# bike_3 = Motorcycle()

# change_color(car_1, "Red")
# change_color(car_2, "White")
# change_color(car_3, "Black")
# change_color(bike_1, "Cyan")
# change_color(bike_2, "Blue")
# change_color(bike_3, "Manokai")

# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)
# print(bike_2.color)
# print(bike_3.color)
# ---------------------------------------------------
# duck typing
# ---------------------------------------------------
# Duck typing = concept where the class of an object is less important than the
#               methods class type is not checked if minimum methods/attributes are
#               present "If it walks like a duck, and it quacks like a duck,
#               then it must be a duck."

# class Duck:

#     def walk(self):
#         print("This duck is walking")

#     def talk(self):
#         print("This duck is qwuacking")

# class Chicken:

#     def walk(self):
#         print("This chicken is walking")

#     def talk(self):
#         print("This chicken is clucking")

# class Person:

#     def catch(self,duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")

# duck = Duck()
# chicken = Chicken()
# person = Person()

# person.catch(duck)

# ----------------------------------------------------
# walrus operator :=
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)
# -----------------------------------------------------

# say = print
# say("Hello World!")
# -----------------------------------------------------
# lambda
# -----------------------------------------------------
# def double(x):
#     return x * 2

# print(double(5))


# double = lambda x:x*2
# multiply = lambda x, y: x * y
# add = lambda x,y,z:x+y+z
# full_name = lambda first_name, last_name:first_name + " " + last_name
# age_check = lambda age:True if age >= 18 else False
# print(age_check(15))
# ------------------------------------------------------
# sort
# ------------------------------------------------------

# students = (("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr. Krabs", "C", 78))

# age = lambda ages:ages[2]
# grade = lambda grades:grades[1]
# name = lambda names:names[0]

# sorted_students = sorted(students, key=age)
# for i in sorted_students:
#     print(i)
# ------------------------------------------------------
# map()
# ------------------------------------------------------
# map() = applies a function to each item in an iterable (list, tuple, etc)

# store = [("shirt", 20.00),
#          ("pants", 25.00),
#          ("jacket", 50.00),
#          ("socks", 10.00)]

# to_euros = lambda data: (data[0], data[1]*0.82)
# to_dollars = lambda data: (data[0], data[1]/0.82)

# store_euros = list(map(to_euros, store))
# store_dollars = list(map(to_dollars, store))

# def toEuros():
#     for i in store_euros:
#         print(i)
# def toDollars():
#     for i in store_dollars:
#         print(i)
# ------------------------------------------------------
# filter()
# ------------------------------------------------------
# filter() = creates a collection of elements from an iterable for which a function
#                                                                          returns
# filter(function, iterable)

# friends = [("Rachel", 19),
#            ("Monica", 18),
#            ("Phoebe", 17),
#            ("Joey", 16),
#            ("Chandler", 21),
#            ("Ross", 20)]

# age = lambda data:data[1] >= 18

# filtered_friends = list(filter(age,friends))

# for i in filtered_friends:
#     print(i)
# ------------------------------------------------------
# reduce() function
# ------------------------------------------------------
# reduce() = apply a function to an iterable and reduce it to a single cumulative
#            value. performs function on first two elements and repeats process
#            until 1 value remains
# reduce(function, iterable)

# import functools

# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x,y:x+y,letters)
# print(word)

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x,y:x*y,factorial)
# print(result)
# ------------------------------------------------------
# list comprehension
# ------------------------------------------------------
# list comprehension = a way to create a new list with less syntax can mimic
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]

# squares = []
# for i in range(10+1):
#     squares.append(i*i)
# print(squares)

# squares = [i * i for i in range(1,11)]
# print(squares)

# students = [100,90,80,70,60,50,40,30,0]
# # passed_students = list(filter(lambda x: x >= 60, students))
# passed_students = [i for i in students if i >= 60]
# print(passed_students)

# ------------------------------------------------------
# dictionary comprehensions
# ------------------------------------------------------
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
# dictionary = {key: expression for (key,value) in iterable}
# ------------------------------------------------------
# zip()
# ------------------------------------------------------
# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, etc)
#                   creates a zip object with paired elements stored in tuples for each element

# usernames = ["Dude", "Bro", "Robin"]
# passwords = ("1234", "Code", "OP")
# usr_passwd = dict(zip(usernames, passwords))

# for key,value in usr_passwd.items():
#     print(key + " : " + value)
# ------------------------------------------------------
# if __name__ == __main__
# ------------------------------------------------------
# y tho?
# 1. Module can run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__

# if __name__ == '__main__':
#     pass

# -------------------------------------------------------
# time module
# -------------------------------------------------------
# import time
# print(time.ctime(1643400000)) # convert a time expressed in seconds since epoch to a
#                               readable string
#                               epoch = when your computer thinks time began
#                                                                 (reference point)
# print(time.time())    # returns current seconds since epoch

# print(time.ctime(time.time()))

 # time_object = time.localtime()
 # print(time_object)
 # local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
 # print(local_time)

# time_string = "January 28, 2022"
# time_object = time.strptime(time_string, "%B %d, %Y")
# print(time_object)

# # (year, month, day, hours, mins, secs, #day of the week, #day of the year, dst)
# time_tuple = (2022, 1, 28, 11, 30, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# # (year, month, day, hours, mins, secs, #day of the week, #day of the year, dst)
# time_tuple = (2022, 1, 28, 33, 30, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)
# -------------------------------------------------------
# thread
# -------------------------------------------------------
# import threading
# import time

# def eat_breakfast():
#     time.sleep(3)
#     print("You had breakfast")

# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffee")

# def study():
#     time.sleep(5)
#     print("You studied")

# x = threading.Thread(target=eat_breakfast, args=())
# x.start()
# y = threading.Thread(target=drink_coffee, args=())
# y.start()
# z = threading.Thread(target=study, args=())
# z.start()

# x.join()
# y.join()
# z.join()

# # eat_breakfast()
# # drink_coffee()
# # study()

# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())
# --------------------------------------------------------
# daemon thread
# --------------------------------------------------------
# daemon thread = a thread that runs in the background, not important for program to
#                 to run, your program will not wait for daemon threads to complete
#                 before exiting, non-daemon threads cannot normally be killed,
#                 stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

# import threading
# import time

# def timer():
#     print()
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("You are logged in for: ", count, "seconds")

# x = threading.Thread(target = timer, daemon = True)
# x.start()

# answer = input("Do you wish to exit?")

# from multiprocessing import Process, cpu_count
# import time

# def counter(num):
#     count = 0
#     while count <= num:
#         count += 1

# a = Process(target=counter, args = (500000000,))
# a.start()
# a.join()

# b = Process(target=counter, args = (500000000,))
# b.start()
# b.join()

# print("finished in ", time.perf_counter(), "seconds")
# ----------------------------------------------------------
# GUI Windows
# ----------------------------------------------------------
# from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

# window.geometry("420x420")
# window.title("robinOP is fire")    these functions are not working on Linux
# icon = PhotoImage(file="path")
# window.iconphoto(True,icon)

# window = Tk() # instantiate an instance of a window
# window.config(background="#5cfcff")
# window.mainloop() # place window on computer screen, listen for events
# ----------------------------------------------------------
# Label
# ----------------------------------------------------------
# from tkinter import *
# #label = an area widget that holds text and/or an image within a window
# window = Tk()
# # photo = PhotoImage(file='/home/robinop/Pictures/ddosqy8-68489511-9d8d-4dec-af2d-35fb1dae7d5a.jpg')
# label = Label(window,
#               text="Hello World!",
#               font=('Fira Mono', 40),
#               fg='Green',
#               bg = 'Black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               )
# label.pack()
# # label.place(x=300,y=400)

# window.mainloop()
# -----------------------------------------------------------
# buttons
# -----------------------------------------------------------
# button = you click it, then it does stuff
# from tkinter import *

# count = 0
# def click():
#     global count
#     count += 1
#     print(count)

# window = Tk()

# button = Button(window,
#                 text="Click me",
#                 command=click,
#                 font=("Fira Mono",30),
#                 fg="Green",
#                 bg="Black",
#                 activeforeground="Green",
#                 activebackground="Black",
#                 state=ACTIVE)

# button.pack()

# window.mainloop()
# -----------------------------------------------------------
# entry box
# -----------------------------------------------------------
# entry widget = textbox that accepts a single line of user input
# from tkinter import *

# def submit():
#     username = entry.get()
#     print("Hello " + username)
#     entry.config(state=DISABLED)

# def delete():
#     entry.delete(0, END)

# def backspace():
#     entry.delete(len(entry.get())-1, END)

# window = Tk()

# entry = Entry(window,
#               font=("Fira Mono", 50),
#               fg="Green",
#               bg="Black")

# entry.insert(0, 'Spongebob')
# entry.pack(side=LEFT)

# submit_button = Button(window, text = "submit", command=submit)
# submit_button.pack(side=RIGHT)

# delete_button = Button(window, text = "delete", command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button = Button(window, text = "backspace", command=backspace)
# backspace_button.pack(side=RIGHT)

# window.mainloop()
# ------------------------------------------------------------
# check_buttons
# ------------------------------------------------------------
# from tkinter import *
# def display():
#     if(x.get()==1):
#         print("You agree!")
#     else:
#         print("You don't agree!")

# window = Tk()

# x = IntVar()

# check_button = Checkbutton(window,
#                            text="I agree to something",
#                            variable = x,
#                            onvalue = 1,
#                            offvalue = 0,
#                            command = display,
#                            font = ('Fira Mono', 20),
#                            fg = "Green",
#                            bg = "Black",
#                            activeforeground="Green",
#                            activebackground="Black",
#                            padx=25,
#                            pady=10)

# check_button.pack()

# window.mainloop()
# -------------------------------------------------------------
# radio button
# -------------------------------------------------------------
# radio button = similar to checkbox, but you can only select one from a group
# from tkinter import *

# food = ["pizza", "hamburger", "french fries"]

# window = Tk()

# for index in range(len(food)):
#     radioButton = Radiobutton(window,
#                               text = food[index], # adds text to radio buttons
#                               variable = x, # groups radiobuttons together if they share same variable
#                               value = index, # assigns each radiobutton a different value
#                               padx = 25, # adds padding on x-axis
#                               font = ("Fira Mono", 50)
#                               )
#     radioButton.pack(anchor=W)

# window.mainloop()
# -------------------------------------------------------------
# scale
# -------------------------------------------------------------
# from tkinter import *

# def submit():
#     print("The temperature is: " + str(scale.get()) + " degrees C")

# window = Tk()

# scale = Scale(window,
#               from_ = 100,
#               to = 0,
#               length = 600,
#               orient = VERTICAL,
#               font = ('Fira Mono', 20),
#               tickinterval = 10,
#               #showvalue = 0
#               resolution = 5,
#               troughcolor = "#69EAFF",
#               fg = "#FF1C00",
#               bg = '#111111')
# scale.pack()

# button = Button(window, text = 'submit', command = submit)
# button.pack()

# window.mainloop()
# -------------------------------------------------------------
# listbox
# -------------------------------------------------------------
# from tkinter import *
# window = Tk()

# def submit():
#     print("You ordered " + listbox.get(listbox.curselection()))

# def add():
#     count_added_item = 6
#     if entry_box.get() != "":
#         listbox.insert(count_added_item, entry_box.get())
#     count_added_item += 1

# def clear():
#     listbox.

# listbox = Listbox(window,
#                   bg = "#f7ffde",
#                   font = ("Fira Mono", 35),
#                   width = 12)
# listbox.pack()

# listbox.insert(1, "pizza")
# listbox.insert(2, "hamburger")
# listbox.insert(3, "hotdog")
# listbox.insert(4, "french fries")
# listbox.insert(5, "pasta")

# listbox.config(height = listbox.size())

# entry_box = Entry(window)
# entry_box.pack()

# submit_button = Button(window,
#                        text = "Submit",
#                        command = submit,
#                        font = ("Fira Mono", 15))
# submit_button.pack()

# add_button = Button(window,
#                     text = "Add",
#                     command = add,
#                     font = ("Fira Mono", 15))
# add_button.pack()

# clear_button = Button(window,
#                       text = "Clear",
#                       command = clear,
#                       font = ("Fira Mono", 15))
# clear_button.pack()

# window.mainloop()
# -----------------------------------------------------
# messagebox
# -----------------------------------------------------
# from tkinter import *
# from tkinter import messagebox

# window = Tk()

# def click():
    # messagebox.showinfo(title = "This is an info message box",
    #                     message = "You are a person")
    # messagebox.showwarning(title = 'WARNING',
    #                        message = "You have a VIRUS!!!!")
    # messagebox.showerror(title = "This is an error message",
    #                      message = "WARNING</SYSTEM-DOWN/>")

  # if messagebox.askokcancel(title = "ask ok cancel",message = "Do you want to do a thing?"):
  #     print("You did a thing!")
  # else:
  #     print("You canceled a thing!")

  # if messagebox.askretrycancel(title = "ask ok cancel",message = "Do you want to retry a thing??"):
  #     print("You retried a thing!")
  # else:
  #     print("You canceled a thing!")

 # if messagebox.askyesno(title = "ask yes or no", message = "Do you like cake?"):
 #     print("I like cake too :)")
 # else:
 #     print("Why do you not like cake !?")

    # answer =  messagebox.askquestion(title = "ask question", message = "Do you like pie?")
    # if answer == "yes":
    #     print("I like pie too :)")
    # else:
    #     print("Why do you not like pie?")
   #  answer = messagebox.askyesnocancel(title = "ask yes no or cancel", message = "Do you like code?")
#     if(answer == True):
#         print("You like to code (:")
#     elif(answer == False):
#         print("Then why are you watching video on coding?")
#     else:
#         print("You have dodged the question!")

# button = Button(window,
#                 command = click,
#                 text = "Click me")
# button.pack()

# window.mainloop()

# ----------------------------------------------------
# colorchooser module
# ----------------------------------------------------
<<<<<<< HEAD
from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg = colorchooser.askcolor()[1])

window = Tk()
window.geometry("420x420")
button = Button(text = 'Click me', command = click)
button.pack()
window.mainloop()
=======
# from tkinter import *
# from tkinter import colorchooser

# def click():
#     window.config(bg = colorchooser.askcolor()[1])

# window = Tk()
# window.geometry("420x420")
# button = Button(text = 'Click me', command = click)
# button.pack()
# window.mainloop()
# ---------------------------------------------------
# text area widget
# ---------------------------------------------------
# text widget = functions like a text area, you can enter multiple lines of text
# from tkinter import *

# def submit():
#     input = text.get("1.0", END)
#     print(input)

# window = Tk()

# text = Text(window,
#             bg = "light yellow",
#             font = ("Ink Free", 25),
#             height = 8,
#             width = 20,
#             padx = 20,
#             pady = 20,
#             fg = "black")
# text.pack()

# button = Button(window,
#                 command = submit,
#                 text = "submit")
# button.pack()

# window.mainloop()
# ---------------------------------------------------
# file dialog
# ---------------------------------------------------
# from tkinter import *
# from tkinter import filedialog

# def openFile():
#     file_path = filedialog.askopenfilename()
#     file = open(file_path, 'r')
#     print(file.read())
#     file.close()

# window = Tk()

# button = Button(text = "Open",
#                 command = openFile)
# button.pack()

# window.mainloop()
# ----------------------------------------------------
# save file
# ----------------------------------------------------
# from tkinter import *
# from tkinter import filedialog

# def saveFile():
#     file = filedialog.asksaveasfile()
#     filetext = str(text.get("1.0", END))
#     file.write(filetext)
#     file.close()

# window = Tk()
# button = Button(text = "Save", command = saveFile)
# button.pack()
# text = Text(window)
# text.pack()
# window.mainloop()
# ----------------------------------------------------
# menu bar
# ----------------------------------------------------
# from tkinter import *
# window = Tk()

# def open_file():
#     print("File has been opened!")

# def save_file():
#     print("File has been saved!")

# def cut():
#     print("You cut some text!")

# def copy():
#     print("You copied some text!")

# def past():
#     print("You pasted some text!")

# menubar = Menu(window)
# window.config(menu=menubar)

# fileMenu = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label="File", menu = fileMenu)
# fileMenu.add_command(label = "Open", command = open_file)
# fileMenu.add_command(label = "Save", command = save_file)
# fileMenu.add_separator()
# fileMenu.add_command(label = "Exit", command = quit)

# editMenu = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label = "Edit", menu = editMenu)
# editMenu.add_command(label = "Cut", command = cut)
# editMenu.add_command(label = "Copy", command = copy)
# editMenu.add_comamnd(label = "Paste", command = paste)

# window.mainloop()
# ----------------------------------------------------
# frame
# ----------------------------------------------------
# frame = a rectangular container to group and hold widgets
# from tkinter import *

# window = Tk()

# Button(window, text = "W", font = ("Fira Mono", 25), width = 3).pack(side = TOP)
# Button(window, text = "A", font = ("Fira Mono", 25), width = 3).pack(side = LEFT)
# Button(window, text = "S", font = ("Fira Mono", 25), width = 3).pack(side = LEFT)
# Button(window, text = "D", font = ("Fira Mono", 25), width = 3).pack(side = LEFT)

# window.mainloop()
# ----------------------------------------------------
# create new window
# ----------------------------------------------------
# from tkinter import *

# def create_window():
#     new_window = Tk()
#     old_window.destroy()
# old_window = Tk()
# Button(old_window, text = "Create new window", command = create_window).pack()
# old_window.mainloop()
# ----------------------------------------------------
# separate tabs
# ----------------------------------------------------
# from tkinter import *
# from tkinter import ttk

# window = Tk()

# notebook = ttk.Notebook(window) # widget that manages a collection of windows/displays

# tab1 = Frame(notebook) # new frame for tab 1
# tab2 = Frame(notebook) # new frame for tab 2

# notebook.add(tab1, text = "Tab 1")
# notebook.add(tab2, text = "Tab 2")
# notebook.pack(expand = True, fill = "both") # expand = expand to fill any space not otherwise
#                                             # fill = fill space on x and y axis

# Label(tab1, text = "Hello, this is tab #1", width = 50, height = 25).pack()
# Label(tab2, text = "Goodbye, this is tab#2", width = 50, height = 25).pack()

# window.mainloop()
# ----------------------------------------------------
# grid geometry manager
# ----------------------------------------------------
# grid() = geometry manager that organizes widgets in a table-like structure in a parent-table
# from tkinter import *

# window = Tk()

# titleLabel = Label(window, text = "Enter your info!", font = ("Fira Mono", 25)).grid(row = 0, column = 0, columnspan = 2)

# firstNameLabel = Label(window, text = "First name: ", bg = "Red").grid(row = 1, column = 0)
# firstNameEntry = Entry(window).grid(row = 1, column = 1)

# lastNameLabel = Label(window, text = "Last name: ", bg = "Blue").grid(row = 2, column = 0)
# lastNameEntry = Entry(window).grid(row = 2, column = 1)

# submitButton = Button(window, text = "SUBMIT", command = submit).grid(row = 4, column = 0, columnspan = 2)

# window.mainloop()
# ----------------------------------------------------
# progress bar
# ----------------------------------------------------
# from tkinter import *
# from tkinter.ttk import *
# import time

# def start():
#     GB = 100
#     download = 0
#     speed = 1
#     while (download<GB):
#         time.sleep(0.05)
#         bar['value'] +=(speed/GB) * 100
#         download += speed
#         percent.set(str(int((download/GB) * 100)) + "%")
#         text.set(str(download) + "/" + str(GB) + " GB completed")
#         window.update_idletasks()

# window = Tk()

# percent = StringVar()
# text = StringVar()

# bar = Progressbar(window, orient = HORIZONTAL, length = 300)
# bar.pack(pady=10)

# percentLabel = Label(window, textvariable = percent).pack()
# taskLabel = Label(window, textvariable = text).pack()

# button = Button(window, text = "Download", command = start).pack()

# window.mainloop()
# ----------------------------------------------------
# canvas
# ----------------------------------------------------
# from tkinter import *
# window = Tk()
# canvas = Canvas(window, height = 500, width = 500)
# # canvas.create_line(0, 0, 500, 500, fill = "Black", width = 5)
# # canvas.create_line(0, 500, 500, 0, fill = "Black", width = 5)
# # canvas.create_rectangle(50,50,250,250)
# # canvas.create_rectangle(100,100,250,250)
# # canvas.create_rectangle(200,200,250,250)
# canvas.create_polygon(250,0,500,500,0,500,fill = "Yellow", outline = "Black", width = 5)
# canvas.pack()
# window.mainloop()
# ----------------------------------------------------
# keyboard events
# ----------------------------------------------------
# from tkinter import *

# def doSomething(event):
#    # print("You pressed: " + event.keysym)
#    label.config(text = event.keysym)

# window = Tk()

# window.bind("<Key>", doSomething)
# label = Label(window, font = ("Fira Mono", 100))
# label.pack()

# window.mainloop()
# --------------------------------------------------
# mouse events
# --------------------------------------------------
# from tkinter import *

# def doSomething(event):
#     print("You did a thing!")

# window = Tk()

# # window.bind("<Button-1>", doSomething)
# # window.bind("<Button-2>", doSomething)
# # window.bind("<Button-3>", doSomething)
# # window.bind("<ButtonRelease>", doSomething)
# # window.bind("<Enter>", doSomething)
# # window.bind("<Leave>", doSomething)
# # window.bind("<Motion>", doSomething)


# window.mainloop()
# --------------------------------------------------
# drag and drop widgets
# --------------------------------------------------
# from tkinter import *

# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y

# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)

# window = Tk()

# label = Label(window, bg = "red", width = 10, height = 5)
# label.place(x = 0, y = 0)

# label2 = Label(window, bg = "blue", width = 10, height = 5)
# label2.place(x = 100, y = 100)

# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)

# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)

# window.mainloop()
# ---------------------------------------------------
# how to move images, widgets, or canvas
# ---------------------------------------------------
# from tkinter import *

# def move_up(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

# def move_down(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

# def move_left(event):
#    label.place(x=label.winfo_x()-10, y=label.winfo_y())

# def move_right(event):
#    label.place(x=label.winfo_x()+10, y=label.winfo_y())

# window = Tk()
# window.geometry("500x500")

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)

# myimage = PhotoImage(file='racecar.png')
#
# label = Label(window,image=myimage)
# label.place(x=0,y=0)

# window.mainloop()
# ------------------------------------------------------
# animations
# ------------------------------------------------------
# from tkinter import *
# import time

# WIDTH = 500
# HEIGHT = 500
# xVelocity = 1
# yVelocity = 1

# window = Tk()

# canvas = Canvas(window, width = WIDTH, height = HEIGHT)
# canvas.pack()

# photo_image = PhotoImage(file = 'path/to/image.png')
# my_image = canvas.create_image(0,0, image = photo_image, anchor = NW)

# image_width = photo_image.width()
# image_height = photo_image.height()

# while True:
#     coordinates = canvas.coords(my_image)
#     print(coordinates)
#     if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0)
#         xVelocity = -xVelocity
#     if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0)
#         yVelocity = -yVelocity
#     canvas.move(my_image,xVelocity,yVelocity)
#     window.update()
#     time.sleep(0.01)

# window.mainloop()
# ----------------------------------------------------
# clock
# ----------------------------------------------------
# from tkinter import *
# from time import *

# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text = time_string)
#     time_label.after(1000,update)

# window = Tk()

# time_label = Label(window, font = ("Fira Mono", 50), fg = "Green", bg = "Black")
# time_label.pack()

# update()

# window.mainloop()
# ----------------------------------------------------
# send email
# ----------------------------------------------------
# import smtplib

# sender = "sender@gmail.com"
# receiver = "receiver@gmail.com"
# password = "password123"
# subject = "Python email test"
# body =  "I wrote an email! :D"

# message = f"""From: Snoop Dogg {sender}
# To: Nicholas Cage{receiver}
# Subject: {subject}\n
# {body}
# """

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()

# try:
#     server.login(sender, password)
#     print("Logged in...")
#     server.sendmail(sender,receiver,message)
#     print("Email has been sent!")
# except smtplib.SMTPAuthenticationError:
#     print("Unable to sign in!")
# ------------------------------------------------
# run py program with terminal
# ------------------------------------------------
# print("Hello World!")

# name = input("What's your name?: ")
# print("Hello " + name)
# ------------------------------------------------
# pip installer
# ------------------------------------------------
# pip = package manager for packages and modules from Python Package Index
#
#       included for Python versions 3.4+
#       open command prompt
#
#       help:                        pip
#       check:                       pip --version
#       update:                      pip install --upgrade pip
#       installed packages:          pip list
#       check outdated packages:     pip list --outdated
#       update a package:            pip install "package name" --upgrade
#       install a package:           pip install "package name"
# ------------------------------------------------
# calculator
# ------------------------------------------------
# from tkinter import *

# def button_press(num):
#     global equation_text
#     equation_text = equation_text + str(num)
#     equation_label.set(equation_text)

# def equals():
#     global equation_text
#     total = str(eval(equation_text))
#     equation_label.set(total)
#     equation_text = total

# def clear():
#     pass

# window = Tk()
# window.title("Calculator program")
# window.geometry("500x500")

# equation_text = ""
# equation_label = StringVar()

# label = Label(window, textvariable = equation_label, font = ("Fira Mono", 20), bg = "White", width = 24, height = 2)
# label.pack()

# frame = Frame(window)
# frame.pack()

# button1 = Button(frame, text = 1, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(1))
# button1.grid(row = 0, column = 0)

# button2 = Button(frame, text = 2, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(2))
# button2.grid(row = 0, column = 1)

# button3 = Button(frame, text = 3, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(3))
# button3.grid(row = 0, column = 2)

# button4 = Button(frame, text = 4, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(4))
# button4.grid(row = 1, column = 0)

# button5 = Button(frame, text = 5, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(5))
# button5.grid(row = 1, column = 1)

# button6 = Button(frame, text = 6, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(6))
# button6.grid(row = 1, column = 2)

# button7 = Button(frame, text = 7, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(7))
# button7.grid(row = 2, column = 0)

# button8 = Button(frame, text = 8, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(8))
# button8.grid(row = 2, column = 1)

# button9 = Button(frame, text = 9, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(9))
# button9.grid(row = 2, column = 2)

# button0 = Button(frame, text = 0, height = 4, width = 9, font = 35,
#                  command = lambda: button_press(0))
# button0.grid(row = 3, column = 0)

# plus = Button(frame, text = '+', height = 4, width = 9, font = 35,
#                  command = lambda: button_press('+'))
# plus.grid(row = 0, column = 3)

# minus = Button(frame, text = '-', height = 4, width = 9, font = 35,
#                  command = lambda: button_press('-'))
# minus.grid(row = 1, column = 3)

# multiply = Button(frame, text = '*', height = 4, width = 9, font = 35,
#                  command = lambda: button_press('*'))
# multiply.grid(row = 2, column = 3)

# divide = Button(frame, text = '/', height = 4, width = 9, font = 35,
#                  command = lambda: button_press('/'))
# divide.grid(row = 3, column = 3)

# equal = Button(frame, text = '=', height = 4, width = 9, font = 35,
#                  command = lambda: button_press('='))
# equal.grid(row = 3, column = 2)

# decimal = Button(frame, text = '.', height = 4, width = 9, font = 35,
#                  command = lambda: button_press('.'))
# decimal.grid(row = 3, column = 1)

# clear = Button(window, text = 'clear', height = 4, width = 12, font = 35,
#                  command = clear)
# clear.pack()

# window.mainloop()
# ------------------------------------------------------------
# tic-tac-toe game
# ------------------------------------------------------------
# from tkinter import *
# import random

# def next_turn(row, column):
#     global player
#     if buttons[row][column]['text'] == "" and check_winner() is False:
#         if player == players[0]:
#             buttons[row][column]['text'] = player
#             if check_winner() is False:
#                 player = players[1]
#                 label.config(text = (players[1] + " turn"))
#             elif check_winner() is True:
#                 label.config(text = (players[0] + " wins"))
#             elif check_winner() == "Tie":
#                 label.config(text = "Tie!")
#         else:
#             buttons[row][column]['text'] = player
#             if check_winner() is False:
#                 player = players[0]
#                 label.config(text = (players[0] + " turn"))
#             elif check_winner() is True:
#                 label.config(text = (players[1] + " wins"))
#             elif check_winner() == "Tie":
#                 label.config(text = "Tie!")

# def check_winner():

#     for row in range(3):
#         if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
#             buttons[row][0].config(bg = "Green")
#             buttons[row][1].config(bg = "Green")
#             buttons[row][2].config(bg = "Green")
#             return True

#     for column in range(3):
#         if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
#             buttons[0][column].config(bg = "Green")
#             buttons[1][column].config(bg = "Green")
#             buttons[2][column].config(bg = "Green")
#             return True

#     if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons [2][2]['text'] != "":
#         buttons[0][0].config(bg = "Green")
#         buttons[1][0].config(bg = "Green")
#         buttons[2][2].config(bg = "Green")
#         return True

#     elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
#         buttons[0][2].config(bg = "Green")
#         buttons[1][1].config(bg = "Green")
#         buttons[2][0].config(bg = "Green")
#         return True

#     elif empty_spaces() is False:
#         return True

#     else:
#         return False

# def empty_spaces():
#     spaces = 9

#     for row in range(3):
#         for column in range(3):
#             if buttons[row][column]['text'] != "":
#                 spaces -= 1

#     if spaces == 0:
#         return False

# def new_game():
#     global player

#     player = random.choice(players)
#     label.config(text = player + " turn")
#     for row in range(3):
#         for column in range(3):
#             buttons[row][column].config(text = "", bg = "#F0F0F0")

# window = Tk()
# window.title("Tic-Tac-Toe")

# players = ["x","o"]
# player = random.choice(players)
# buttons = [[0,0,0],
#            [0,0,0],
#            [0,0,0]]

# label = Label(text = player + " turn", font = ("Fira Mono", 40))
# label.pack(side = "top")

# reset_button = Button(text = "Restart", font = ("Fira Mono", 20), command = new_game)
# reset_button.pack(side = "top")

# frame = Frame(window)
# frame.pack()

# for row in range(3):
#     for column in range(3):
#         buttons[row][column] = Button(frame, text = "", font = ("Fira Mono", 40), width = 5, height = 2,
#                                       command = lambda row = row, column = column: next_turn(row, column))
#         buttons[row][column].grid(row = row, column = column)

# window.mainloop()
# ----------------------------------------------------------
# snake game
# ----------------------------------------------------------
# from tkinter import *
# import random

# GAME_WIDTH = 700
# GAME_HEIGHT = 700
# SPEED = 50
# SPACE_SIZE = 50
# BODY_PARTS = 3
# SNAKE_COLOR = "#00FF00"
# FOOD_COLOR = "#FF0000"
# BACKGROUND_COLOR = "#000000"

# class Snake:
#     def __init__(self):
#         self.body_size = BODY_PARTS
#         self.coordinates = []
#         self.squares = []

#         for i in range(0, BODY_PARTS):
#             self.coordinates.append([0,0])

#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
#             self.squares.append(square)

# class Food:
#     def __init__(self):
#         x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
#         y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

#         self.coordinates = [x,y]

#         canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")

# def next_turn(snake, food):
#     x, y = snake.coordinates[0]

#     if direction == "up":
#         y -= SPACE_SIZE

#     elif direction == "down":
#         y += SPACE_SIZE

#     elif direction == "left":
#         x -= SPACE_SIZE

#     elif direction == "right":
#         x += SPACE_SIZE

#     snake.coordinates.insert(0, (x, y))
#     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
#     snake.squares.insert(0, square)

#     if x == food.coordinates[0] and y == food.coordinates[1]:
#         global score
#         score += 1
#         label.config(text = "Score:{}".format(score))
#         canvas.delete("food")
#         food = Food()

#     else:
#         del snake.coordinates[-1]
#         canvas.delete(snake.squares[-1])
#         del snake.squares[-1]

#     if check_collisions(snake):
#         game_over()
#     else:
#         window.after(SPEED, next_turn, snake, food)

# def change_direction(new_direction):
#     global direction

#     if new_direction == 'left':
#         if direction != 'right':
#             direction = new_direction

#     elif new_direction == 'right':
#         if direction != 'left':
#             direction = new_direction

#     elif new_direction == 'up':
#         if direction != 'down':
#             direction = new_direction

#     elif new_direction == 'down':
#         if direction != 'up':
#             direction = new_direction


# def check_collisions(snake):
#     x, y = snake.coordinates[0]
#     if x < 0 or x >= GAME_WIDTH:
#         return True

#     elif y < 0 or y >= GAME_HEIGHT:
#         return True

#     for body_part in snake.coordinates[1:]:
#         if x == body_part[0] and y == body_part[1]:
#             print("GAME OVER")
#             return True

#     return False

# def game_over():
#     canvas.delete(ALL)
#     canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
#                        font = ("Fira Mono", 70), text = "GAME OVER", fill = "red", tag = "gameover")

# window = Tk()
# window.title("Snake game")
# window.resizable(False, False)

# score = 0
# direction = 'down'
# label = Label(window, text = "Score:{}".format(score), font = ("Fira Mono", 40))
# label.pack()

# canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
# canvas.pack()

# window.update()

# window_width = window.winfo_width()
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# x = int((screen_width/2) - (window_width/2))
# y = int((screen_height/2) - (window_height/2))

# window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# window.bind("<Left>", lambda event: change_direction('left'))
# window.bind("<Right>", lambda event: change_direction('right'))
# window.bind("<Up>", lambda event: change_direction('up'))
# window.bind("<Down>", lambda event: change_direction('down'))

# snake = Snake()
# food = Food()

# next_turn(snake, food)

# window.mainloop()
