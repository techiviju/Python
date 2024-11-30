"""
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
"""

n=int(input("Enter Number :-"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    print("*"*(2*(n-i)+1))

for j in range(1,n+1):
    if(j!=1):
        print(" "*(n-j),end="")
        print("*"*(2*j-1))