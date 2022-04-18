# # Removing elements from a dictionary
# # create a dictionary
# squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# # remove a particular item, returns its value
# # Output: 16
# print(squares.pop(4))
# # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# print(squares)
# # remove an arbitrary item, return (key,value)
# # Output: (5, 25)
# print(squares.popitem())
# # Output: {1: 1, 2: 4, 3: 9}
# print(squares)
# # remove all items
# squares.clear()
# # Output: {}
# print(squares)
# # delete the dictionary itself
# del squares
# # Throws Error
# # print(squares)
# print("**"*20)
# square = {}
# for x in range(6):
#     square[x] = x*x
# print(square)

print("**"*20)
items =	{
  "center": "Ford",
  "location": "adyar",
  "year": 2000,
"coaching":["python","java","selenium"]
}
# for x, y in items.items():
#   print(x, y)
# print("**"*20)
# print("**"*20)
# mydict = items.copy()
# print(mydict)
# mydic = dict(items)
# print(mydic)
# for value in items.keys():
#   print(value)