# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# vehicle = {
#   "brand": ["Ford","suzuki"],
#   "model": "Mustang",
#   "year": 1964
# }
# print("example for dic---->",vehicle)
# print("dictionary value printed here---->",vehicle["brand"])
# print("*=*"*50)
# # dictionary wont allow  duplicate keys but it will allow duplicate values)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2021,
#   "year": 2020
# }
# print("duplicate keys  removed here",thisdict)
# print("length of the dictionar",len(thisdict))
# print("*=*"*50)
# thisdict1 = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict1)
# print(type(thisdict1))
# x = thisdict1["brand"]
# print(x)
# print(thisdict1.keys())
# y= thi)sdict1.values()
# print(y)
# print("*=*"*50

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["updated year"] = 2020
print(x) #after the change
y=car.keys()
print(y)
print(car.items())
car["brand"]=["toyota","suzuki",]
print(car.items())
car.update({"year": 2020})
print(car.items())
# x = car.values()
# print(x) #before the change
# print(type(x))
# #add new key inside the dictionay
# car["color"] = "red"
# print(x) #after the change
# print("*=*"*50)
# print(car.items())
# print(type(car.items()))
# print("*=*"*50)
# if "model" in car:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# print("*=*"*50)
# #update the dictionay
# cardict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# cardict.update({"year": 2020})
# print(cardict)
# print("*=*"*50)
#
# dictdel = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# dictdel.popitem()
# dictdel.pop("model")
# print(dictdel)
# # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):