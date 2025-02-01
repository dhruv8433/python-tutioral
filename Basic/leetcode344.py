# arr = ['h', 'e', 'l', 'l', 'o']

# def reverseString(s):
#     # custom logic for reverse
#     for i in range(len(s)):
#         s.insert(i, s.pop())
#     return s

# print(reverseString(arr))

def calculatePrice(distance, minutes):
    # calculate price
    price = 0
    if (distance < 50 and minutes < 30): # distance between o to 50 and minutes between 0 to 30
        price = 10
    elif (distance < 100 and minutes < 60): # distance between 50 to 100 and minutes between 30 to 60
        price = 20
    elif(distance >= 100 and minutes >= 60): # distance above 100 and minutes above 60
        price = 30
    
    return price

distance = 70
minutes = 40
price = calculatePrice(distance, minutes)
print('total price for required distance ' , distance  , 'and taking time ' , minutes , 'should be :' , price ,'$')

