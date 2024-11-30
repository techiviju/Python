'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

n=int(input("Enter Your Number :-"))
for i in range(1,n+1):
    if(i!=n):
        print(" "*(n-i),end="")
        print("*"*(2*i-1))
    
for j in range(1,n+1):
    print(" "*(j-1),end="")
    print("*"*(2*(n-j)+1))
