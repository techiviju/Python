# Hollow triangle star Pattern
'''
        *
        **
        * *
        *  *
        *   *
        ******
'''

n=int(input("Enter Your Number:- "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*i)
    else:
        print("*",end="")
        print(" "*(i-2),end="")
        print("*")
