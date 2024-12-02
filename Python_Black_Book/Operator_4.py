    #Arithmatic Operator -> 7
'''
power=5**3  
print(power)

floor=(1+2)*3**2//2+3 #floor
print(floor)
'''
    #Assignment Operator 74
'''
a,b=1,5
print(a,b)
'''

'''
a=3; b=5
if(a<b):
    print("yes")
else:
    print("NO")
'''
    
    #bitwise operator
#bitwise operators perform operations on the binary representations of integers at the bit level.
# 6 types

    #Unary Operator
#when this operator is used before a variable,it's value is negative.
'''
n=8
print(~n) # -9 # bitwise complement op
m=-8
print(~m) # 7
'''

        #Relational Operator.
'''
x=15
print(10<x<20)  # true

print(10>=x<20) # false
print(10<x>20)  # false

print(1<2<3<4<5)  #true
print(1>0<5>5<3)    #false
print(5<9>=5>2)     #true
'''

    #Logical Operator
'''
x=100
y=200
print(x and y) # 200 if x is false then return x. otherwise y
print(x or y) # 100 if x is false then return y. otherwise x

print(not x) # if x is false then return true. otherwise false.
'''

    #Boolean
'''
a=True
b=False
print(a,b)

print(a and a) # true  # boolean and op
print(a and b) # false
print(b and b) # false
print("==================")
print(a or a) # true    #boolean or op
print(a or b) # true
print(b or b) # false

print(not a)
print(~a)
'''

    #Bitwise operator
'''
x=10
y=20
print('~x=',~x) # -11

print('x&y=',x&y) # 0  bitwise and op
print('x|y=',x|y) # 30  bitwise or op

print('x^y=',x^y) # 30  XOR
print('x<<2=',x<<2) # 40    bitwise left shift 

print('x>>2',x>>2) # 2  bitwise right shift
'''

    # membership operator 84
'''
name=["vijay","rohit","mohit","shreyash","adi"]
for names in name:
    print(names)
'''
 
    # tow membership operator 1) in 2) not in

'''
postal={"chandrapur":442401,"Bhadravati":442402,"Gondpipari":442702}
for post in postal:
    print("Membership op",post,postal[post])
'''

    #Identity operator // memory location. 85
a=25
b=25
print(id(a))
print(id(b))

        #Two types of identity operator. 
            #is , is not
if(a is b):  #check memory address (identity nu) if same then true otherwise false.
    print("a and b have same")
else:
    print("a and b have different")

one=[1,2,3,4]
two=[1,2,3,4]

print(id(one))
print(id(two))
if(one is two):
    print("one and two have same")
else:
    print("one and two have different")