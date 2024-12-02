import sys
import argparse
'''
n=len(sys.argv)  #n is the number of arguments
args=sys.argv  # args list contains arguments
print("nu of command lines :-",n)  # Enter values at run time
print("the args are:-",args)

for a in args:
    print(a)
'''

'''
#Program 18
v1=int(sys.argv[1])
v2=int(sys.argv[2])
print("sum is = ",v1+v2)
'''
        #   OR
'''
sum=int(sys.argv[1])+int(sys.argv[2])
print("sum is =",sum)
'''

    #Pragram 19 
'''
args=sys.argv[1:]
print(args)
print(type(args))
sum=0
for a in args:
    x=int(a)
    if x%2==0:
        sum+=x
print("the sum is =",sum)
'''

# print("my name is vijay")