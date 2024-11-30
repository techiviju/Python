# Write a program to find whether a given number is prime or not.

num=int(input("Enter the nu :-"))

for i in range(2,num):
      if(num%i)==0:
            print(f"{num} is a not prime number")
            break
else:
      print(f"{num} is a prime number")