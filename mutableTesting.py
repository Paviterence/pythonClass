# list is mutable or changeable
s=[1,2,3,4]
print(s)
print("before id ---->",id(s))
s.append("hi")
print(id(s))
print(s)
print("**"*30)
#tuple tuple is immutable or unchangable
t=(1,2,3,4)
print(t)
print("before id ---->",id(t))
l=list(t)
l.append("hi")
t=tuple(l)
print(t)
print(id(t))
print("**"*30)
#set unchangable or immutable
Set={1,2,3,4,3}
print(Set)
print(id(set))
Set.add(8)
print(Set)
print(id(Set))
print(Set)
print("**"*30)
#dictionary is changeable or mutable
d={}
print(id(d))
print(type(d))
d[12]="hi"
d[13]="hello"
d[14]="welcome"
d[15]="greens"
print(d)#dictionary is created
print(type(d))
print(id(d))