'''
 ***   ***
***** *****
***********
 *********
  *******
   *****
    ***
     *
'''

n = int(input("Enter Your Number : "))
for i in range(1,n+1):
  print(" "*(n-i),end="")
  print("* "*(i),end="")

  print(" "*(2*(n-i-1)),end="")
  if(i!=n):
    print("* "*(i),end="")
  if(i==n):
    print("* "*(i-1),end="")
  print()

