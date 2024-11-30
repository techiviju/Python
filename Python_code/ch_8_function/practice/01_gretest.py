# 1. Write a program using functions to find greatest of three numbers.

def gretest():
      nu1=int(input("Enter First Number :-"))
      nu2=int(input("Enter Second Number :-"))
      nu3=int(input("Enter Third Number :-"))

      if(nu1>nu2 and nu1>nu3):
            return nu1
      elif(nu2>nu1 and nu2>nu3):
            return nu2
      elif(nu3>nu1 and nu3>nu2):
            return nu3

print("The Greatest Number is ",gretest())