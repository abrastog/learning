#!/usr/bin/python
#abhay = [ ]
#for i in range(7, 10):
#    a = i 
#    abhay.append(i)
#print(abhay)

my_movies = [['How I Met Your Mother', 'Friends', 'Silicon Valley'],
    ['Family Guy', 'South Park', 'Rick and Morty'],
    ['Breaking Bad', 'Game of Thrones', 'The Wire']]


for i in my_movies:
    for j in i:
        abhay = len(j)
        print (" the tille of " + j + " is " + str(abhay) + " long ")

