#!/usr/bin/python


name = " Abhay:rastogi "
company = "vmware"
print(name.strip())
print (name.lower())
print(name.upper())
print (name.replace(":", "-"))


temp = "my name is {1} and i m working in {0}".format(name, company)
print(temp)
print (name + company)

temp1 = f"my name is {company} and i m working in {name}"
print(temp1)
