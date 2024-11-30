# Hollow Pyramid Pattern In Python

n=int(input("Enter Your Number:- "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    if(i==1 or i==n):
        print("*"*(2*i-1))
    
    else:
        print("*",end="")
        print(" "*(2*i-3),end="")
        print("*")
        