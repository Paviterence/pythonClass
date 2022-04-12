thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(thislist)
print("=*done*="*10)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print("=*done*="*10)
#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print("=*done*="*10)

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
print("=*done*="*10)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
print(list1.count("a"))
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
# reverse the order of list elements
prime_numbers.reverse()

print('Reversed List:', prime_numbers)
# Output: Reversed List: [7, 5, 3, 2]

prime_number = [11, 3, 7, 5, 2]

# sort the list
prime_number.sort()
print(prime_number)

# Output: [2, 3, 5, 7, 11]


# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop() 	Removes the element at the specified position
# remove()	 Removes the item with the specified value
# reverse() 	Reverses the order of the list
# sort()	 Sorts the list
