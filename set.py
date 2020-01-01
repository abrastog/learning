#!/usr/bin/python


abhi = {1,2,3,3,4,5,65}

a = type(abhi)
print(a)
abhi.add(33) #for addding element in set 

#abhi.remove(55)
"""it will give error bcoz der is no 55 present in set 
answer:-
Traceback (most recent call last):
  File "set.py", line 10, in <module>
    abhi.remove(55)
KeyError: 55
"""
#abhi.discard(55)
"""
it will not give any error as we know der is no 55 in set
rabhay-a01:python_utube rabhay$ python set.py
<type 'set'>
set([1, 2, 3, 4, 5, 65, 33])

"""
#abhi.discard(65)
"""
rabhay-a01:python_utube rabhay$ python set.py
<type 'set'>
set([1, 2, 3, 4, 5, 33])

"""

"""
if u wanna added multiple thg in this set use "update command"
"""
abhi.update([2,55,33,22,22,11])
print(len(abhi))
"""
rabhay-a01:python_utube rabhay$ python set.py
<type 'set'>
10
set([1, 2, 3, 4, 5, 65, 11, 22, 55, 33])

"""
b =  abhi[1]
print(b)
print (abhi)
