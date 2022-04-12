import keyword
print(keyword.kwlist)
Keywords='''['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 
'except', 'finally', 'for', 'from', 'global', 'if',import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield '''#reserved words to python we cannot use as a variable
variable="no spaces,do not start with number"
datatypes="i am string",1,1.2,True
print(datatypes)
n=10
print(type(n))#describe the class
print(id(n))#memory allocation
no=5.6e2
print(no)
no=12.5
print(type(no))
# ctrl+f10
#ctr+shift+f10

# complex data types its in python only
# it contains real and imaginary part 5+6j ,ust enter j only
value=5+6j
print(value.real)
print(value.imag)
Input_=input("enter anything")
output=print("i am print")

#boolean in python its bool its gives True or False and its case sentitive
mark1=96
mark2=98
print(mark1>mark2)
print(mark1<mark2)
print(mark1==mark2)#== which consider true or false
print(True+False)#true=1 and false=0
print(True+True)
print(False+False)#0
#string
name='pavi'
print(name)
name="pavi"
print(name)
address='''pavithran
from chennai'''
print(address)
print('hi\npavi')#\n for next line
print('hi\tpavi')#\tspace
sentence="'thiruvalluvar' wrotes 'thirukural'"
print(sentence)
sente=''''thiruvalluvar' wrote "thirukural"'''
