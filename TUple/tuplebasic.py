# #tuple practice
# '''tuple items are ordered, unchangeable, and allow duplicate values.
#
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#
# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
#
# '''
# tuple1 = ("abc", 34, True, 40, "male")
#
# print(tuple1)
#
# a="boeing","airbus"
# print(a)
# a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# b=tuple(a)
# print(b)
# #cocatenation of tuple
# a1="boeing","airbus"
# b1=0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# c=(a1+b1)
# print(c)
# print(a1,b1)#nesting of tuple
# print(a,b)
# print(c,a)
# #repetition in tuples
# a=("python",)*5
# print(a)
# b=(1,2,3,4,5,6,7,8,9,10)*2
# print(b)
# print(a,b)
# #tuples are  immutable so we can't  replace any value in tuples
# h=list(range(50,1,-2))
# print(tuple(h))
# print(len(h))
# print(h[1:])#slicing of tuples
# print(h[:20])
# print(tuple(h[::-1]))
# hello=(0,1,2,3)
# print(hello[::-1])
# print(hello)
# my_name=input("enter you name:")
# n=int(input("enter number of time to repeat your name :"))
# for i in range(int(n)):
#     print(my_name)
#
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])
# #if you want add anything into the tuple you need to convert it as a list
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)
#
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
#
# print(thistuple)
#
# # When we create a tuple, we normally assign values to it. This is called "packing" a tuple
# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)
# #len() function for tuple
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))
#
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")
#
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])
#
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
print(thistuple.count("apple"))
print(thistuple.index("apple"))
# # Method	Description
# # count()	Returns the number of times a specified value occurs in a tuple
# # index()	Searches the tuple for a specified value and returns the position of where it was found