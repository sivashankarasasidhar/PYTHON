# remove repeated character from string 
str = input()
result = ""
repeat = set()
for char in str:
    if char not in repeat:
        result += char 
        repeat.add(char)
print(result)