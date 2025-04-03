# string is muttable menas we can change the value of string
# a="hellu"
# this will print hellu
# print(a)

# this will print mumma
# a="mumma"
# print(a)


# string is immutable we can not change
# a="riddhu"
# a[0]="h"
# we can not change like this
# TypeError: 'str' object does not support item assignment


#  casefold()=>convert to lower
# name="heLLyy"
# print(name.casefold())
# print(name.lower())

# upper=>convert to upper and not change in exsting string
# print(name.upper())


#  rstrip()=>convert ! chacracter to none
# name1="helLUU!!!!@@@@@@"
# print(name1.rstrip("@"))
# print(name1.rstrip("!"))


# replace()=>replace the name
# name1="hellu"
# print(name1.replace("hellu","riddhu"))



# split()=>its split the sentence
# name1="hellu hii howare you"
# print(name1.split(","))
# output:['hellu hii howare you']


# capitalized=>convert first letter to caplital and rest convert in lower
# name="hello helli"
# print(name.capitalize())




# center()=>convert string to centr we have to define space count
# name="hello helli"
# print(len(name))  output:11
# print(name.center(50))
# print(len(name.center(50)))    output:50 it allocate 39 space




# name="hello helli"
# print(name.count("l")) //4




# endswith give answer in true or false
# str1="welcome to the console"
# print(str1.endswith("to",4,10))
# name="hello$$"
# print(name.endswith("$$"))




# find()=>find the first occurance word and return the index if not match than 
# retunrs -1
# str1="welcome to the console"
# print(str1.find("to"))
# print(str1.find("m"))



# index()=>same as find but give error if word not found 



# isalnum()=>return true if str cotain a-z A-Z 0-9
# str1="HEllo1hellu"
# print(str1.isalnum())

# isalpha=>return true when its have a-z and A-Z
# str1="HEllo1hellu"
# print(str1.isalpha())


# isprintable()=>return false when we use /n


# isspace()=>return true if string conatin whitespace it only rteurn true when tehre is aplhabet
# str1="       "          //true
# str2="  hellu     "  //false
# print(str1.isspace())  
# print(str2.isspace())


# istitle=>return true if first letter caplitailized of each word
# str1="Hello Hellu"
# print(str1.istitle())


# swapcase()=>lowercase to upprrcase uppercase to lowercase
# str1="hello"
# print(str1.swapcase())


# titlr()=>first letter of each word capital
# str1="hell hloo kese ho"
# print(str1.title())

















