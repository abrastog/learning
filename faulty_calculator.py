#!/usr/bin/python


num1 = int(raw_input("Enter the value :- "))
num2 = int(raw_input("Enter the value :- "))



opr = raw_input ("Enter the operator here:-  \n (+)\n (-)\n (*)\n (/)\n" )

if opr == "+":
    if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print ("sum is :-  77")
    else:
        print ("print value of sum %r,%r is :- " %(num1, num2))
        print(num1+num2)

if opr == "-":
    if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print ("sum is :-  100")
    else:
        print ("print value of sum %r,%r is :- " %(num1, num2))
        print(num1-num2)

if opr == "*":
    if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45:
        print ("sum is :-  555")
    else:
        print ("print value of sum %r,%r is :- " %(num1, num2))
        print(num1*num2)

if opr == "/":
    if num1 == 56 and num2 == 6 or num1 == 6 and num2 == 56:
        print ("sum is :-  4")
    else:
        print ("print value of sum %r,%r is :- " %(num1, num2))
        print(num1/num2)
