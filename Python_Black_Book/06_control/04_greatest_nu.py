# Print the greatest number

n1,n2,n3=int(input("Enter 1st nu :-")),int(input("Enter 2nd nu :-")),int(input("Enter 3rd nu :-"))

if(n1>n2 and n1>n3):
    print("Number 1 is large :",n1)
elif(n2>n1 and n2>n3):
    print("Number 2nd is large :-",n2)
else:
    print("number 3rd is large :-",n3)