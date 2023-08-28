# check given string is palindrome or not 
# example 1 
str = input()
lower = str.lower()
str_2 = str[::-1]
if str == str_2:
    print("given str is palindrome")
else:
    print("given str is not palindrome")