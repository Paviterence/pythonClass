# try:
#     a=int(input("enter number1 \n:"))
#     b=int(input("enter number2\n:"))
#     c = a / b
# except ZeroDivisionError as msg:
#     # print("there is error in try block the except block is executed")
#     print(" this statement is raising an arithematic exception")
#     print(msg)
# else:
#     print("if there is no error in try block the else block is automatically executed")
#     print(c)
#     print("success")
# finally:
#     print("I executed at last ")
#     d=100+100
#     print(d)
#print error as a msg
# try:
#     a=int(input("enter the value of a :"))
#     b=int(input("enter the value of b :"))
#     c=a/b
#     print("the division of c :",c)
# except Exception as msg:
#     print("this statement raising an arithematic exception")
#     print(msg)
# #generic method
# try:
#     a = int(input("enter the value of a :"))
#     b = int(input("enter the value of b :"))
#     c = a / b
#     print("the division of c :", c)
# except:
#     print("this statement raising an arithematic exception")

age=int(input("enter your age:"))
# raise TypeError("enter string only ")
if age < 18:
    raise Exception("age should be less than 18")
else:
    print("permitted for voting")

