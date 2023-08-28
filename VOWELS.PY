str = "aeiou"
word = input()
if word.isalpha() :
    if word in str:
        print("vowel")
    else:
        print("not vowel")
else:
    print("Invalid input")