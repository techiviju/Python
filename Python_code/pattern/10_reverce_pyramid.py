'''
********* 9
 *******  7
  *****   5
   ***    3
    *     1
'''
n=int(input("Enter Your Number :-"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    print("*"*(2*(n-i)+1))