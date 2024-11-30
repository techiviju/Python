import random
'''
1 for snake
-1 for water
0 for gun
'''

computer=random.choice([-1,0,1])
youstr=input("Enter Your str  like (s,w/g):-")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]

reverseDict = {1:"snak",-1:"water",0:"gun"}

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}\n")

if(computer == you ):
    print("Match Draw :---")
else:

    if(computer == -1 and you == 1):  # 2
        print("You Win!")

    elif(computer == -1 and you == 0):  # -1
        print("You Win!")

    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Lose!")
    
    elif(computer == 0 and you == 1):
        print("you Lose!")

    else:
        print("something went wrong")