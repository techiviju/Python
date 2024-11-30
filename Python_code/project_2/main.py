import random
n=random.randint(1,100)

guess=1
a=-1

while(a!=n):
    if guess > 10:
        print("You have exceeded the maximum number of attempts is 10. Please try again.")
        break  
    a=int(input("Enter you Guess number :- "))
    if(a>n):
          print("Enter Lowest Number :- ")
          guess+=1

    elif(a<n):
         print("Enter Highest Number :- ")
         guess+=1

if(a==n):
    print(f"You have guessed the number {n} correctly in {guess} attempts")