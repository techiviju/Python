    #Chapter 5 Input and Output.
    # Output statement
#print(3*'hello vijay\n')    #print 3 times

#print("city name "+"Chandrapur") # + concatinate
#print("city name","Chandrapur") # , separating the str

a,b=4,5
#print(a,b,sep="----")  # separate the string using that car or synbol.

#print("hello ",end='') # print str at the end of the line using end attribute.
#print("vijay ",end='')
#print("bhau")

#print("hello",end='\t')
#print("programmer")

'''
name="vijay"
print("formatted =%i int"%a)
print("hii %20i"%name)  # allot 20 caces

print("hii (%-20s)"%name) #allot after name space

print("%c,%c used dispay single char"%(name[0],name[1]))
print("hi %s"%name[0:3]) #print str start from 0 and end from 3 = vij
'''
'''
num=123.23654
print("float %18.3f"%num) # 18 is indecate of space bet float and value, and 3 is floating nu 
'''
'''
n1,n2,n3=5,6,9
print('number1={0}'.format(n1)) #format field is used to replace the values

print("number1= {0}, number2 = {1} number3 = {2}".format(n1,n2,n3))

print("n1={two} n2={three} n3={one}".format(one=n1,two=n2,three=n3))

print("num1={} num2={} num3={}".format(n1,n3,n3))
name,salary="vijay",23203.23
print("name = {:s} salary = {:.1f}".format(name,salary))

print("nu1={1} nu2={0} nu3={2}".format(n1,n2,n3))
'''

    # Input Statement
'''
str=input("Enter your name :-")
print("your name is",str)
num=int(input("Enter your age :-"))
print("age is = ",num)
'''
    # Program 3
#Accept single characte
'''
ch=input("Enter a char :-")
print("you entered = ",ch[0])
'''

    #Program 4
'''
num=int(input("Enter number :-"))
print("the nu is = ",num)
'''    #program 6
# accept only float nu
'''
fl=float(input("Enter float nu :- "))
print("float nu is = ",fl)
'''
    # program 7 pg 103
'''
nu1=int(input("Enter nu 1 :-"))
nu2=int(input("Enter nu 2 :-"))
print("addition is =",nu1+nu2)

print("addition is = {}".format(nu1+nu2))
'''
    # program 10
'''
str=input("Enter Binary nu :- ")
bin=int(str,2)
print("bin interger =",bin)

str=input("Enter Octal :-")
oct=int(str,8)
print("oct to int =",oct)

str=input("Enter Hexa:-")
hexa=int(str,16)
print("hexa to int=",hexa)
'''
    #Program 11
'''
var1,var2,var3=[int(x)for x in input("Enter three nu:-").split()]
print("sum is =:-",var1+var2+var3)
'''

    # Program 12 106
'''
var1,var2,var3=[int(x)for x in input("Enter three Number :").split(",")]
print("sum is :- ",var1+var2+var3)
'''

    #Program 13
'''
str1,str2,str3={str(x)for x in input("Enter three string separated by , :- ").split(",")}
print("string is :- ",str1,str2,str3)
'''
    # OR
'''
lst=[x for x in input("Enter str , :- ").split(",")]
print("lst :- ",lst)
'''

    #Program 14  107
'''
a,b=10,23
#result=eval('a+b+5')
#print(result)

print(eval('a+b+5'))
'''

    # Program 15 
'''
x=eval(input("Enter the lst :- "))
print(x)
'''
    #program 16
'''
tpl=eval(input("enter tpl :-"))
print("tpl:-",tpl)
'''
        # Command line arg
    #Program 17 109
# Display command line argument  cmd.py (file)
_
