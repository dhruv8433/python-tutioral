# data types have 2 types
# 1. Mutable data types
# 2. Immutable data types

# Mutable data types
# 1. List
# 2. Dictionary
# 3. Set

# Immutable data types
# 1. int
# 2. float
# 3. bool

# numbers
a =5 
print(type(a))
a = 5.3
print(type(a))
a = 5 + 3j
print(type(a))

# string
s = "hello@dhruv12"
print(type(s))

# list - immutable, sequence of items
l = [1, 2, 3, 'hi']
print(type(l))

# tuple - immutable, ordered and more then 1 value compulsory
t = (1, 2, 3, 'hi')
print(type(t))

# dictionary - immutable, unordered, key value pair
d = {1: 'one', 2: 'two'}
print(type(d))
print("access index 1 from dict :",d[1])

# set - immutable, unordered, unique values, ignore duplicate values
s = {1, 2, 3, 4, 5, 1}
print("set: ",s,type(s))

# taking user input
# name = input("Enter your name: ")
# print("Hello",name)

# conditional statement
# no = int(input("Enter no: "))
# if(no%2 == 0):
#     print("Even")
# else:
#     print("Odd")

# simple calc using conditions
# print("welcome to calc")
# a = int(input("Enter 1st no: "))
# b = int(input("Enter 2nd no: "))
# op = input("Enter operator(+, -, *, /): ")
# if(op == '+'):
#     print("Addition: ",a+b)
# elif(op == '-'):
#     print("Subtraction: ",a-b)
# elif(op == '*'):
#     print("Multiplication: ",a*b)
# elif(op == '/'):
#     print("Division: ",a/b)

# loops
# for loop
print('\n')
for i in range(5):
    print(i)

print("\n")
for i in range(2,5):
    print(i)

print("\n")
for i in range(1,10,2):
    print(i)

# while
print("\n")
i = 0
while(i<5):
    print(i)
    i += 1