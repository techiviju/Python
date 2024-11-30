# Left Downward Triangle Pattern

n=int(input("Enter Your Number : "))

for i in range(0,n):
    if(i==0):
        print("*"*n)
    else:
        print("*"*(n-i))
        
   
    