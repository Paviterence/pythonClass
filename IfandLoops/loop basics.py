#
# # Python program to illustrate
# # Iterating over a list
# print("List Iteration")
# l = ["geeks", "for", "geeks"]
# for i in l:
#     print(i)
#
# # Iterating over a tuple (immutable)
# print("\nTuple Iteration")
# t = ("geeks", "for", "geeks")
# for i in t:
#     print(i)
#
# # Iterating over a String
# print("\nString Iteration")
# s = "Geeks"
# for i in s :
#     print(i)
#
# # Iterating over dictionary
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d :
#     print("%s %d" %(i, d[i]))
#
# # Iterating over a set
# print("\nSet Iteration")
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i),
# # Python program to illustrate
# # Iterating by index
#
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
	print (list[index])
# # Python program to illustrate
# # combining else with for
#
# list = ["geeks", "for", "geeks"]
# for index in range(len(list)):
# 	print list[index]
# else:
# 	print "Inside Else Block"
# # Prints all letters except 'e' and 's'
for letter in 'greenstech':
	if letter == 'e' or letter == 's':
		continue
	print ('Current Letter :', letter)
