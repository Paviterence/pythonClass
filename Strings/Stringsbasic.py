#string slicing
import  string

# a = "SeleniuM!"
# print("1st--->",a[1])
# print('**'*10)
# print("2nd---->",a[5])
# print('**'*10)
# print("3rd--->",a[1:6])
# print('**'*10)
# print("4th---->",a[:4])
# print('**'*10)
# print("5th--->",a[::2])
# print('**'*10)
# print("6th--->",a[::-1])
# print('**'*10)
# print(a.isascii())
# print('**'*10)
# print(a.upper())
# print('**'*10)
# print(a.lower())
# print('**'*10)
# print(a.capitalize())
# print('**'*10)
# print(a.isalnum())
# print('**'*10)
# print(a.isalpha())
# print('**'*10)
# print(a.isdigit())
# print('**'*10)
# print(a.swapcase())
# print('**'*10)
# # Program to find the ASCII value of the given character
# c = 'p'#character value is findout here
# print("The ASCII value of '" + c + "' is", ord(c))
# letters=string.ascii_uppercase
# print(letters)
# print('**'*10)
# print((',').join(letters))
# print('**'*10)
#interview question
# x = "   Hello, World!   "
# # The strip() method removes any whitespace from the beginning or the end
# print(x)
# print(x.strip())
# print(x.replace("Hello","welcome to python"))
# print(x.replace(" ",""))
# y="eiiieee"
# print(y.replace("e","a",3))
# print(y.replace("e","a",2))

# split method split the string and gives string as a substring as a array
# str1="python,selenium,java"
# str2=str1.split(",")
# lenstr=len(str1)
# print(lenstr)
# print(str2)
# for i in str2:
#     print(i)
#
# for length in range(len(str2)):
#     print(str2[length])

# cocatenation
# a = "Hello"
# b = "World"
# c = a + b
# print(c)
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# reverse word and content of letters
s="python is very easy compare to other language"
l=s.split()
print(len(l))#count the words in a string
# l2=l[::-1]
print(l)
l3=[]
for word in l:
    l3.append(word[::-1])
print(" ".join(l3))