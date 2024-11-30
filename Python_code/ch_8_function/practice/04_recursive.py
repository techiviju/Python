# 4. Write a recursive function to calculate the sum of first n natural numbers.

def natural(n):
      if(n==1):
            return 1
      return natural(n-1) + n

n=int(input("Enter Natural number :-"))
print(natural(n))
