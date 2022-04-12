#it will print every element present in the sequence
#
# for no in range(50,2,-2):
#     print(no,end=",")
#
# # print(list(range(50,2,-2)))
#
# for  n in [0,1,2]:
#     print(n,end=',')

# a=["pavi","naren","haji"]
# for i in range(10):
#     print(",".join(a))
#add of enter value
# a=int(input("enter the value of a: "))
# b=int(input("enter the value of b: "))
# r=int(input("how many times you waNT"))
# c=a+b
# sum=0
# for i in range(r):
#     sum=sum+c
#     print(sum)
#repeat the string value
# a=input("enter the value of a: ")
# b=input("enter the value of b: ")
# c=a+b
# for i in range(5):
#     print(c)
# print odd numbers
# start=int(input("enter the starting range value: "))
# end=int(input("enter the ending range value: "))
# for i in range(start,end+1):#(10,11,12,13,14,15,16,17,18,19,20)
#     if(i%2==0):
#         print(i,end='  ,') sep,round,min,max
# #print even numbers
# start=int(input("enter the starting range value: "))
# end=int(input("enter the ending range value: "))
# for i in range(start,end+1):
#     if(i%2==0):
#       print(i)

# for letter in 'greenstech':
# 	if letter == 'e' or letter == 's':
# 		continue
# 	print ('Current Letter :', letter)
# 	var = 10

#addition of number
# total=1
# number=int(input("enter the number series:"))
# for no in range(1,number+1):
#     total=total+no
#     print(no,end=", ")
#
# print("addtion of series with given number",total)
#
# #factorial or given number
# 5!=5*4*3*2*1


# total=1
# number=int(input("enter the number :"))
# for no in range(1,number+1):
#     total=total*no
#     print(no,end=", ")
#
# print("factorial of series with given number",total)

#words count
# sentence="welcome to greens tech"
# wordscount=1
# for letter in sentence:
#
#     if letter==" ":
#         wordscount+=1
#     # print(letter,end=" ")
# print("number of words are present in the sentence",wordscount)

#prime number or not 2,3,5,7,11,13,17,19
no=int(input("enter any number :\n"))
for i in range(2,no):
    if(no%i==0):
        print("NOT prime")
        break
else:
    print("prime")




