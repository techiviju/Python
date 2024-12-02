'''
     #convet number to bin,oct,hex
a=10
b=bin(a)
print("binary",b)

o=oct(a)
print("oct = ",o)

h=hex(a)
print("hexa = ",h)
'''
#convert octa,bin,hexa to int
'''
n1=0o45
n2=0b010111
n3=0x2c45

n=int(n1)
print("octal = ",n)

n=int(n2)
print("Binary = ",n)

n=int(n3)
print("Hexadecimal = ",n)
'''
#Convert string to oct,binary,hexa to int
'''
s1="45"
s2="010111"
s3="2c45"

n=int(s1,8)
print("Octal 45 = ",n)

n=int(s2,2)
print("Binary 010111 = ",n)

n=int(s3,16)
print("hexa = 2c45 = ",n)
'''
     
        # list data type []
# Represent the group of element.
# list can store different type of element but array can store only one type of element.

'''
element=[10,12,20,255]
print(element)

print(element[1])
print(element[-1])

print(element[2:4])
print(element*2)

ele2=["vijay","ajay"]
'''
        #byte datatype
#in byte type array we cannnot edit or modified.
#only allowed positive int values 0 to 255
#cannot be modified
'''
b=bytes(element)
print("type b ", type(b))

for i in b:print(i)

'''
        #bytearray datatype
#similar to the byte but it can be modified.
'''
element3=[20,60,70,40,25]
x=bytearray(element3)
#for j in x:print(j)
x[0]=99
for l in x:print(l)
'''

    #tuple datatype
#similar to the list. contain group of element () 
# not modified (read only list)
'''
tpl=(10,-20,"vijay",60.20,"ajay")
print(tpl[0])

print(tpl[-2])
#print(tpl*2)

print("1 to 5 ",tpl[1:5])
#for x in tpl:print(x)
'''

    # range datatype 60

#r=range(10)
#for i in r:print(i)
'''
r=range(20,41,2) # start range ,end , increament
for i in r:print(i)
'''

    # sets 61
# unorder collection of ele..
#not accept dublicate values

    # set datatype {}
'''
s={10,20,10,15,30}
print(s)

ch=set("vijay")
print(ch)

lst=[1,3,6,7,0,"vijay"]
s=set(lst)
print(s)

s.update([50,40])
print(s)

s.remove(3)
print(s)
'''
    #Frozenset datatype 62
#same as a set but it can not be modified.
'''
s={60,30,80,'hema',1}
fr=frozenset(s)
print(fr)

fs=frozenset("mukesh")
print(fs)
'''
    #Mapping Types
#map represent a group of elements in the form of key and values pairs.
'''
d={1:"vijay",2:"Shreyash",3:"Rohit",4:"tanmay"}
#print(d)
#print(d[1])
print(d.keys())
print(d.values())

d[1]="Ajay"     #update
del d[4]  #delete
print(d)
'''

    #Literals 
#literal is a constant value that is store into a variable in a program.
    
    #Numeric literal
#a=15 # 15 is a literal

    #Boolean literal
# true and false

    #string literal
'''
s1= 'my name is vijay chaudhari this is my job to find out the code \v and im a programmer'
print(s1)
'''

    #Determinig the datatype of a variable 65
#everything is class in python
'''
a=20
b=10.5
c='vijay'
d=[10,30,60,80]
e={99,77,80}
f=(11,65,85,44)

print("a is ",type(a))
print("b is ",type(b))
print("c is ",type(c))
print("d is ",type(d))
print("e is ",type(e))
print("f is ",type(f))
'''
str="Vijay"
upper=str[0].isupper()
print(upper)
strr='''hello my name is vijay
and what is your name 
thanks for inroll this course...'''
print(strr)
