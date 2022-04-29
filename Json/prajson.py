import json

myjasonfile=open("D:/new 5.json")
jsandata=myjasonfile.read()
a=json.loads(jsandata)
# print(a)
a["name"]="pavi"
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a)
#update json file with values
a.update( {
"brand": "Ford",
"model": "Mustang",
"year": 1964
})
print(a)
