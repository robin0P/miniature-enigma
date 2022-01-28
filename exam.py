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
from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg = colorchooser.askcolor()[1])

window = Tk()
window.geometry("420x420")
button = Button(text = 'Click me', command = click)
button.pack()
window.mainloop()
