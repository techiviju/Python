'''
    *
   * *
  *   *
 *     *
*       *  9
 *     *   7 
  *   *    5
   * *
    *
'''

n=int(input("Enter Number :-"))
for i in range(1,n):
    if(i==1):
       print(" "*(n-1),end="")
       print("*")
    elif(i!=n or i!=(n+1)-n):
        print(" "*(n-i),end="")
        print("*",end="")
        print(" "*(2*i-3),end="")
        print("*")
        
for j in range(1,n+1):
    if(j==1):
        print("*",end="")
        print(" "*((2*(n-j))-1),end="")
        print("*")
    elif(j!=n):
        print(" "*(j-1),end="")
        print("*",end="")
        print(" "*((2*(n-j))-1),end="")
        print("*")
    elif(j==n):
        print(" "*(j-1),end="")
        print("*")
