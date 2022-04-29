# Python_Collections ="""(Arrays)
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members. indexed,modified
#
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. indexed
#
# Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
#
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
#
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
#
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered
# """
#
# list="""
# Lists are used to store multiple items in a single variable.
#
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#
# Lists are created using square brackets"""
#
# pavi = ["apple", "banana", "cherry"]
# print(pavi)
# print("id for this list---->",id(pavi))
# print((type(pavi)))
# print("=*"*50)
#
# """List items are ordered, changeable or mutable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc."""
# #Replace
# print(pavi[0])
# pavi[0]='Replaced'#ordered
# print(pavi)
# pavi.insert(0,"hello")#inserted without change the order
# print(pavi)
# print("id is same after insert and replaced check here----->",id(pavi))
#
# print("=*"*50)
# #
# list2= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # lenth function shows how many values inside the list
# print(len(list2))#7 =0,1,2,3,4,5,6 in negative index -1.-2.-3
# print(list2.index("apple"))
# # lists are indexed
# print(list2[0])
# print(list2[2])
# print(list2[-1])
# print(list2[-2])
# print(list2[0:2])
# print(list2[2:4])
# print(list2[:4])
# print(list2[2:])
# print("=*"*50)
# if "apple  " in list2:
#   print("Yes, 'apple' is in the fruits list")
# else:
#     print("not in the list")
# print("=*"*50)
#
# list3= ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# list3[1:3] = ["blackcurrant", "watermelon","butterfruit"]
#
# print("=*"*50)
# #slice index work with order
# list4 = ["apple", "banana", "cherry"]
# list4[1:2] = ["watermelon"]
# print(list4)
# print("=*"*50)
# #insert To change the value of a specific item, refer to the index number:
# list5= ["apple", "banana", "cherry"]
# list5.insert(2, "watermelon")#we need to mention index and value for replace
# print(thislist)
# print("=*"*50)
# #append
#To add an item to the end of the list, use the append() metho
# list6 = ["apple", "banana", "cherry"]
# list6.append("orange")#extend
# print(list6)
# print("=*"*50)
# # Remove Specified Item remove()
# The remove() method removes the specified item.
# thislist1= ["apple", "banana", "cherry","banana"]
# thislist1.remove("banana")#value mention
# print(thislist1)
# print("=*"*50)
# # Remove Specified Index pop()
# The pop() method removes the specified index.
thislist2 = ["apple", "banana", "cherry"]
# print(thislist2.pop(0))
# print(thislist2)
# print("=*"*50)
# The del keyword also removes the specified index:\pr
# print(thislist2)
# # del thislist2[2]
# thislist2.clear()
# print(thislist2)
# # The clear() method empties the list.
# # The list still remains, but it has no content.
# thislist2.clear()
# print(thislist2)
# try:
#     del thislist2
#     print(thislist2)
# except:
#     print("list deleted")
# thislist3 = [True, "banana", "cherry"]
# mylist = thislist3.copy()
# print(thislist3)
# print(mylist)
#
# thislist4 = ["apple", "banana", "cherry"]
# mylist = list(thislist4)
# print(mylist)
# #add two list
list1 = ["a", "b", "c"]
list2 = (1, 2, 3)
# list3 = list1 + list2
# print(list3)
list1.extend(list2)
print(list1)
list1.append(list2)
print(list1)

