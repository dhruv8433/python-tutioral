user_input = input("Enter String for checking is it palindrome or not: ")

if user_input == user_input[::-1]:
    print("Yes, it is palindrome")
else:
    print("No, it is not palindrome")


# Another way to check palindrome
for i in range(0, len(user_input)):
    # user_input = madam
    # userin[0] = m and length of user_input = 5 - 0 - 1 = userin[4]
    if user_input[i] == user_input[len(user_input) - i - 1]:
        print("Yes, it is palindrome")
        break
    else:
        print("No, it is not palindrome")
        break