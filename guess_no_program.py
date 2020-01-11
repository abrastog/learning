#!/usr/bin/python


Guess = 0
value = 33

while(Guess < 9):
    Guess = Guess + 1
    number = int(raw_input("enter ur no :--- "))
    if value > number :
        print("enter value is lesser than result")
    elif value == number :
        print ("you enter the correct number")
        print "you took %r chance to give correct answer" %(Guess)
        print "NOw your game is over"
        break
    else :
        print("value is greater ")
