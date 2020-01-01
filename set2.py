#!/usr/bin/python


set1 = set()
set2 = set()

a = type(set1)
print(a)


for i in range(1,7):
    set1.add(i)

for j in range(4,9):
    set2.add(j)

print(set1)
print(set2)

"""
set([1, 2, 3, 4, 5, 6])
set([8, 4, 5, 6, 7])
"""

set3 = set1.union(set2)
print(set3)

"""
set([1, 2, 3, 4, 5, 6, 7, 8])
"""
set3 = set1.intersection(set2)
print(set3)


set1.clear()
print(set1)
