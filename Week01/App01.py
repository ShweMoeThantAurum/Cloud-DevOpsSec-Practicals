# Question 1 - Develop an application that asks the user for her/his name, and then greets them with their name.

from Program01 import Greeting
username = input("Enter your username: ")
print(Greeting.do_greeting(username))