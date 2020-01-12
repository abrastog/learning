#!/usr/bin/python


def abhay():
    appuchu =  "here we are writing 1st function"
    return appuchu #always use return function in ur program


print (abhay())   





""" here we are talking about doc string in python """

a = int(raw_input("enter the value here:-"))
b = int(raw_input("enter the value here:-"))

def abhi(a,b):
    """ here we are using this function to take 2 input and do sum of them """
    sum = (a+b)
    return sum


print(abhi.__doc__)
v = abhi(a,b)
print "value of abhi function is :-", v
