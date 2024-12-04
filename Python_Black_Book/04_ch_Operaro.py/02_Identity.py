a=25

b=25

print("Id a :-",id(a),"id b :-",id(b))

# is operator

if (a is b):
    print("id is same")

else:
    print("Id is not same")

x=[2,3,4]
y=[2,3,4]

print("Id X:-",id(x)," Id of Y :-",id(y))

if (x is y):
    print("id is same of x and y")

else:
    print("Id of x and y is not same")