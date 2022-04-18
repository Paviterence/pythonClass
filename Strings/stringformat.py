#string formatting
# print("hello"+20)
print("hello",20)#its not concate we are just passing the parametr into the print statement
print("hello"+str(20))
try:
    age = 36
    txt = "My name is John, I am " + age
    print(txt)
except:
    print("syntax error")
# The format() method takes the passed arguments, formats them,
# places them in the string where the placeholders {} are\
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print("*"*50)
quantity = 3
itemno = 567
price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
print("I want {} pieces of item {} for {} dollars.".format(quantity, itemno, price))#must follow the parameter order
# print(myorder.format(quantity, itemno, price))
print("I want {} pieces of item {} for {} dollars.".format( itemno, price,quantity))
print("*"*50)
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."#index is based on the format(0,1,2,3,4)
print(myorder.format(quantity, itemno, price))
print("*"*50)

age = 36
name = "John"
txt = "His name is {1},{1} is {0} years old."
print(txt.format(age, name))
# print(txt.format(name,age))
print("*"*50)

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))