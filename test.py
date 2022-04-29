a="my name is pavithran"
# l=a[::-1]
# print(l)
#
# l1=a.split()
# print(len(l1))
# print(l1[3][::-1])

# rev=reversed(a)
# print("".join(rev))
s=a.split()
s1=s[::-1]
s2=[]
i=0
while i>len(s1):
    s2.append(s1[i])
    i -=1
print(s2)

Product_list = {'P 01': 'DBMS', 'P 02': 'OS',
                'P 0 3 ': 'Soft Computing'};

# removing spaces from keys
# storing them in sam dictionary
Product_list = {x.replace(' ', ''): v
                for x, v in Product_list.items()}

# printing new dictionary
print(" New dictionary : ", Product_list)