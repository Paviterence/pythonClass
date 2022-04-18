# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# some JSON:
import json

x = '{ "name":"John", "age":30, "city":"New York"}'
try:
    print(x["age"])
except:
    print('json file not parse with python')
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y)

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
print(type(y))


# You can convert Python objects of the following types, into JSON strings:
#
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
