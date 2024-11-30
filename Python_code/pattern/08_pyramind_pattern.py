# The pyramid pattern has an odd number of stars in each row 1, 3, 5, 7, etc.
'''
    *
   ***
  *****
 *******
*********
'''

n=int(input("Enter Your Number:- "))
for i in range(1,n+1):
       
   print(" "*(n-i),end="")
   print("*"*(2*i-1))
        
