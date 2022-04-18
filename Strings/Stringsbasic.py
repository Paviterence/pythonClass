# #string slicing
# a = "Selenium!"
# print("1st--->",a[1])
# print("2nd---->",a[5])
# print("3rd--->",a[1:6])
# print("4th---->",a[:4])
# print("5th--->",a[::2])
#
# print(a.upper())
# print(a.lower())
# print(a.capitalize())

# x = "   Hello, World!   "
# # The strip() method removes any whitespace from the beginning or the end
# print(x)
# print(x.strip())
# print(x.replace("Hello","welcome to python"))
# y="eiiieee"
# print(y.replace("e","a",3))
# print(y.replace("e","a",2))

# split method split the string and gives string as a substring as a array
str1="python,selenium,java"
str2=str1.split(",")
lenstr=len(str1)
print(lenstr)
print(str2)
for i in str2:
    print(i)

for length in range(len(str2)):
    print(str2[length])

# cocatenation
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)