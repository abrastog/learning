#!/usr/bin/python

print ("enter the no1 :- ")
num1 = input()
print(type(num1))

print ("enter the no2 :- ")
num2 = str(input())
print(type(num2))

try:
    print ("this is sum of two value",
       int(num1) + int(num2))
except Exception as e:
    print(e)

print ("here we cross the Exception")
