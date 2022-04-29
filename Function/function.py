# predefined function
# selenium,mysql
# functions with variables
# A function is a block of code[set of instruction] which only runs when it is called.
# remove(value)
# welcome(name)
# welcome(pavi)
# You can pass data, known as parameters, into a function.
# def ---> is the keyword to initiate the function
def welcome(name=None,lastnaME=None):
    print("welcome to python class",name,lastnaME)
welcome("pavi","S")
welcome(lastnaME="s",name="pavi")
welcome("pavi")
welcome("hi","how are you")
welcome()
# error hint
#you have to call the function with 2arguments, not more, and not less.
# def hi():
#     print("hi")
# hi()
# def plus(a,b):
#     print(a+b)
# plus(10,20)
# def username(name):
#     print("name")


# function within class is called method(function def)

#
# types of aruguments
# positional argumengt---works based on the postion
# keyword arugument--you need to mention
# default arugument---it will take default arguments values untill we give valuee for that
# variable arugument