#!/usr/bin/python


number = int(raw_input("Enter the numner here:- "))

while(True):
    if number < 100:
        print (number)
        number = number + 1
    if number >= 100:
        print("congratulation ur no is greater than  or equal to 100")
        break
