# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
WhileLoop="""In python, while loop is used to execute a block of statements 
repeatedly until a given condition is satisfied.
And when the condition becomes false, the line immediately after 
the loop in the program is executed."""

# while expression:
#     statement(s)

# i = 1#initilalize
# # condition
# # increement
# while i <= 100:##1<6 6<6  multilple
#   print(i)
#   i += 1#increement
#
# # if 12>11:
# #     print("true")

#
# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Geek")
# print("loop is completed")
#
# count = 0
# while (count == 0): print("Hello Geek")
#
# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# i= 1
# while i < 6:
#     # print(i)
#     if i == 3:
#         break
#     print(i)
#     i += 1

i= 1
while i < 6:
    # print(i)
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# word count
# name=input("enter the name:")
# length=len(name)
# print("length of the name",length)
# i=0
# count=1#to count the spaces
# while i<length:
#     if name[i]==' ':
#         count+=1
#         #print(name[i])
#     i=i+1
# print("no of words in the sentence",count)
#
# name=input("enter the name:")
# length=len(name)
# print("length of the name",length)
# i=0
# count=0#to count the vowels
# while i<length:
#     #if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u':
#     if name[i] in ['a','e','i','o','u']:
#         count+=1
#         print(name[i])
#     i+=1
# print('number of vowels in the name',count)