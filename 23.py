from os import replace 

#changing two strings using replace() Method
'''str1="THIS IS DEVELOPMENT project"
str2="Testing"
str3=str1.replace("DEVELOPMENT",str2)
print(str3)
-----------------------------------------------------
str1="OUR CLIENT IS APPLE"
str2="SAMSUNG"
str3=str1.replace("APPLE",str2)
print(str3)
-----------------------------------------------------
str1="PROJECT NAME TEMPLERUN"
str2="BATTELGROUND"
str3=str1.replace("TEMPLERUN",str2)
print(str3)'''

#supparating the strings using the split() Method
'''str1="I AM WORKING IN PYTHON DEVELOPMENT"
str2=str1.split(" ")
print(str2)'
---------------------------------------------
str1="I,AM,WORKING,IN,PYTHON,DEVELOPMENT"
str2=str1.split(",")
print(str2)
---------------------------------------------
str1="I@AM@WORKING@IN@PYTHON@DEVELOPMENT"
str2=str1.split("@")
print(str2)'''

#joining group of string in type of (list,typle) with respective seperator
'''str1=["python","java","testing"]
str2="".join(str1)
print(str2)
--------------------------------------
str1=["python","java","testing"]
str2=",".join(str1)
print(str2)
--------------------------------------
str1=["python","java","testing"]
str2=";".join(str1)
print(str2)'''

#in and not, not in operators
'''str1="siva shankara sasidhar"
lis=[1,23,4,23,4]
tup=("boss","manager","developer","trainer")
print( 1 in lis)
print("boss" in tup)
print("siva" in str1)
----------------------------------------------------------------
str1="siva shankara sasidhar"
lis=[1,23,4,23,4]
tup=("boss","manager","developer","trainer")
print( 1 not lis)
print("boss" not tup)
print("siva" not str1)
---------------------------------------------------------------
str1="siva shankara sasidhar"
lis=[1,23,4,23,4]
tup=("boss","manager","developer","trainer")
print( 1 not in lis)
print("boss" not in tup)
print("siva" not in str1)'''

#remove spaces from the string 
'''s= 'm a r o l i x'
str1=s.replace(" ",'')
print(str1)
--------------------
s= 'd e v e l o p e r'
str1=s.replace(" ",'')
print(str1)
---------------------
s= 'p y t h o n'
str1=s.replace(" ",'')
print(str1)'''

#comparing two strings
'''str1="python"
str2="java"
if str1>str2:
    print("it is greater")
elif str1<str2:
    print("it is false")
elif str1==str2:
    print("equal")
------------------------------------
str1="java"
str2="python"
if str1>str2:
    print("it is greater")
elif str1<str2:
    print("it is false")
elif str1==str2:
    print("equal")
------------------------------------'''

#finding the substring by using index
'''str = 'Python is fun'
result = str.index('is')
print(result)
-----------------------------
str = 'Python is fun'
result = str.index('fun')
print(result)
-----------------------------
str = 'Python is fun'
result = str.index('python')
print(result)'''

#using rindex()
'''str1 = "this is string"
str2 = "is"
print(str1.rindex(str2))
print(str1.index(str2))
--------------------------------
str1 = "this is python"
str2 = "python"
print(str1.rindex(str2))
print(str1.index(str2))
---------------------------------
str1 = "this is not java it was easy"
str2 = "not"
print(str1.rindex(str2))
print(str1.index(str2))'''

# finding the substring by using find()
'''python = "Hello world!"
finding = python.find("w")
print(finding)
------------------------------------
python = "development"
finding = python.find("e")
print(finding)
-------------------------------------
python = "testing"
finding = python.find("t")
print(finding)'''

#finding the substring by using rfind()
'''str1 = 'siva shankara sasidhar'
str2= str1.rfind('sasi')
print(str2)
-----------------------------------
print(str1.rfind('siva', 5, 20))
print(str1.rfind('sasi', 0, 30)) 
print(str1.rfind('dhar', 0, -1))'''