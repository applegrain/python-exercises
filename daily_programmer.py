__author__ = 'Applegrain'
#1 Create a program create a program that will ask the users name, age, and reddit username. have it tell them
# the information back, in the format: your name is ", you are " years old, and your username is ".

name = raw_input("name:")
age = int(raw_input("age:"))
username = raw_input("username:")

print ("Your name is %s, your are %r years old and your reddit username is %r." % name,age,username)
