# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

n1=int(input("Enter python marks :-"))
n2=int(input("Enter cpp marks :-"))
n3=int(input("Enter java marks :-"))
n4=int(input("Enter c marks :-"))

total=n1+n2+n3+n4
percentage=total/4
print("total",total)

if(n1>=33 and n2>=33 and n3>=33 and n4>=33):
      print("your all sub is clear")
      if(percentage>=40):
            print(f"Congratulation your pass \nyour percentage is {percentage}%")
else:
      print(f"sorry your faile {percentage}%")


