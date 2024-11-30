# Write a program to print multiplication table of n using for loops in reversed
# order.

nu=int(input("Enter the number :-"))

for i in range(1,11):
      print(f"{nu}X{11-i} =",(11-i)*nu)