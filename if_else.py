#!/usr/bin/python

print ("welcome to RTO office please fill the form")

AGE = int(raw_input("Please enter ur age here :- "))

if AGE>18:
    print ("You are eligible to drive")
elif AGE==18:
    print ("Please come for verification")
elif AGE<18:
    print ("You are minor for this")
else:
    print ("wrong input")
