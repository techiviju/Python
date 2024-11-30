'''
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *
'''

n=int(input("Enter Your Number :-"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(i))

for j in range(1,n+1):
    if(j!=5):
        print(" "*(j),end="")
        print("*"*(n-j))