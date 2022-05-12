#TRY and EXCEPT errors handling
#we need enter the errors statments in TRY section and in except statment  we need enter what type of error

#basic
"""a=10/0
print(a)"""
#this is zerodivision error we cannot divide the number with zero it gives infinity so we need to tell
#the user your entered value is exception of operations
#Zerodivision error
#pr:1
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

# #pr:2
# try:
#     a=10/2
#     print(a)
# except ZeroDivisionError:
#     print(" this statement is raising an arithematic exception")
# else:
#     print("success")
# #pr:3 ArithmeticError
# try:
#     a=10/2
#     print(a)
# except ArithmeticError:
#     print(" this statement is raising an arithematic exception")
# else:
#     print("success")
#
# #pr:4 without mentioning error
# """
# try:
#     a=int(input("enter the value of a :"))
#     b=int(input("enter the value of b :"))
#     c=a/b
#     print("the division of c :",c)
# except:
#     print("this statement raising an arithematic exception")"""
#
# #pr:5 lookup error orIndexError: list index out of range
# """a=[1,2,3,4]
# print(a[5])"""
# try:
#     a=[1,2,3,5]
#     print(a[6])
# except LookupError:
#     print("list index out of bound error")
# else:
#     print("success")
# #key error mostly occured in dictionary function
# dict={'a':1,'b':2,'c':3}
# print(dict['a'])
# #print(dict['d'])#KeyError: 'd'
# try:
#     dict = {'a': 1, 'b': 2, 'c': 3}
#     print(dict['a'])
#     print(dict['d'])#KeyError: 'd'
# except KeyError:
#     print("key error")
# #class and object using try and exception method
# try:
#     class test:
#         def division(self, a, b):
#             div= a / b
#             return div
#
#
#     a = int(input("enter the vale of a: "))
#     b = int(input("enter the value of b:"))
#     divide = test()
#     div=divide.division(a, b)
#     print("division of given value id :", div)
# except ZeroDivisionError:
#     print("this statement raising an arithmetic exception")
# except ValueError:
#     print("this statement raising an arithmetic exception, pls enter number only")
#
# #value error
# try:
#     print(int('a'))
# except ValueError:
#     print('value error')
# try:
#     class test:
#         def subraction(self, a, b):
#             sub= a - b
#             return sub
#
#
#     a = int(input("enter the vale of a: "))
#     b = int(input("enter the value of b:"))
#     minus = test()
#     sub=minus.subraction(a, b)
#     print("subraction of given value  :", sub)
# except ValueError:
#     print("this statement raising an arithmetic exception pls enter numbers only")
# #positive or negative using functions with exceptions
# try:
#     def number(a):
#         if (a%2==0):
#             print("positive")
#         else:
#             print("negative")
#             return a
#     a=int(input("enter the number"))
#     num=number(a)
#     print(num)
# except:
#     print("value error enter the number")
# finally:
#     print("program completed")

#type 1 exception with comments
# try:
#     age=int(input("enter your age:"))
#     if age>17:
#         raise Exception("AGE SHOULD BE GREATER THAN 18")
#         # print("permitted for voting")
#     else:
#         print("age should be less than 18")
# except Exception as msg:
#     print(msg)

# type 2 raise with comments
# try:
#     age=int(input("enter your age:"))
#     if age<18:
#         raise ValueError("age should be less than 18")
#     else:
#         print("permitted for voting")
# except ValueError as msg:
#     print(msg)
#
# #type 3 without try and exception it gives the error

age=int(input("enter your age:"))
# raise TypeError("enter string only ")
if age < 18:
    raise ValueError("age should be less than 18")
else:
    print("permitted for voting")

# #type 4 using class and object raise with comments
# class humantemprature:
#     def __init__(self,temp):
#         self.temp=temp
#     def check_temp(self):
#         if  self.temp >97:
#             #print("you are suffering from fever")
#             raise Exception("temprature abnormal")
#         elif self.temp<88:
#             #print("you are suffering from cold fever")
#             raise Exception(" temprature abnormal")
#         else:
#             print('you are normal cheerup')
# check=humantemprature(int(input("enter the temp: ")))
# check.check_temp()
