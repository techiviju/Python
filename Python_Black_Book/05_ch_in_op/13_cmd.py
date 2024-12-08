# Display Command line Argument

import sys

n=len(sys.argv)  #Number of arg

args=sys.argv   # args list contains arguments

print("The Number of command lines args :-",n)
print("The args are:-",args)

print("the args one by one:")
for a in args:
    print(a)