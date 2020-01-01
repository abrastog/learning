#!/usr/bin/python

var1 = int(raw_input("Enter the 1st no here : "))

var2 = int(raw_input("Enter the 2nd no here : "))

calc = str(raw_input("take any input Sum/diff/multiply/division : "))

if (calc == "Sum"):
   print(var1 + var2)
elif (calc == "diff"):
   print (var1 - var2)
elif (calc == "multiply"):
   print(var1 * var2 )
elif (calc == "division"):
   print(var1 / var2)
else:
   print("wrong input")

  
