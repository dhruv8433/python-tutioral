# print 
print("Hello world")
print ('Hi there', '''this will print 
       same
       as i write ''')


# variables
a = 10
b = 20
c = a + b
print(c)

a = 14

# same location for a and b take a garbadge value
print(id(a), id(b), id(a))


# type of variable
a = 10
print(type(a))

# another way to define a variable
a = b = c = 10

# naming style variable
a = 10
a_b = 10
a_b_c = 10

# string
a = "Hello"
b = 'World'
c = a + ' ' + b
print(c)

# arithmetics operations
a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# comparison operators
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# assignment operators
a += b
print(a)

# membership operators
a = [1, 2, 3, 4]
print(1 in a)
print(5 in a)

# identity operators
a = 10
b = 10
print(a is b)
print(a is not b)

# bitwise operators
print(a & b)
print(a | b)
print(a ^ b)

# to find binary 
print(bin(a))
print(bin(b))