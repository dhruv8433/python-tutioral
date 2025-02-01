# this code find prime numbers between 2 user input ranges

range1 = int(input("Enter no 1: "))
range2 = int(input("Enter no 2: "))


for i in range(range1, range2):
    if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        print(i)
    i += 1