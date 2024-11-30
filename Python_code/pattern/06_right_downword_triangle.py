# Right Downward Triangle Pattern

n=int(input("Inter Your Number :- "))

for i in range(n):
    if(i==0):
         print("*"*n)
    else:
        print(" "*i,end="")
        print("*"*(n-i))
        