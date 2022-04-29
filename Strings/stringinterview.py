#reverse a string
# a=input("enter the sting to reverse: \n")
# r=a[::-1]#reverse the character
# print(r)
# for i in r:#print one by one
#     print(i)
# method:2
# r=reversed(a)
# print(''.join(r))
# method:3 using string
# s="my name is pavi"
# i=len(s)-1
# output=""
# while i>len(s):
#     output=output+s[i]
#     i -=1
# print(output)

#reverse a words
# s="python is very easy compare to other language"
# l=s.split()
# print(l)
# reversel=l[::-1]
# print("  ".join(reversel))
#reverse word and content of letters
# s="python is very easy compare to other language"
# l=s.split()
# print(len(l))#count the words in a string
# l2=l[::-1]
# print(l)
# l3=[]
# for word in l2:
#     l3.append(word[::-1])
# print(" ".join(l3))

#reverse secon word content in a string
# s="one two three four five"
# l=s.split()
# lenl=len(l)
# print(lenl)
# l1=[]
# for i in range(lenl):
#     if i%2==0:
#         l1.append(l[i])
#     else:
#         l1.append(l[i][::-1])
# print(l1)

# s="one two three four five"
# l=s.split()
# i=0
# l2=[]
# while i<len(l):
#     if i%2==0:
#         l2.append(l[i])
#     else:
#         l2.append(l[i][::-1])
#     i +=1
# print(" ".join(l2))

# # Iterating through a string
# count = 0
# for letter in 'Hello World':
#     if(letter == 'l'):
#         count += 1
# print(count,'letters found')


str = 'cold'
# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
#character count
print('len(str) = ', len(str))
str.isascii()