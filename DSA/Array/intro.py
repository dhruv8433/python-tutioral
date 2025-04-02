from array import *

a1 = array('i', [10, 20, 30]) # i - signed int
print(type(a1)) # <class 'array.array'>

for x in a1:
    print(x)

a1.append(40) # append 40 to the end of the array
print(a1) # array('i', [10, 20, 30, 40])

print(a1.count(10)) # count the number of occurrences of 10 in the array
# 1