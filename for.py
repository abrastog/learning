#!/usr/bin/env python


a = int(raw_input("Enter the no here :- "))

for i in range(a, 20):
    if i % 2 == 0 and i % 4 == 0:
        print ("Number " + str(i) + " is divided by 2 and 4")
    elif i % 2 == 0:
        print("Number " + str(i) + "is divided by 2")
    elif i % 4 == 0:
        print ("Number " + str(i) +  "is divided by 4")
    else:
        print("-------")
    



