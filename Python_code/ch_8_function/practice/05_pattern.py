# Write a python function to print first n lines of the following pattern:
# ***
# **
# *            - for n = 3

def pattern():
      n=int(input("Enter number :-"))
      for i in range(1,n+1):
            print(("*"*(n-i+1)))
            
pattern()