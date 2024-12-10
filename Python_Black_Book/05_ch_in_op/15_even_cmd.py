# find sum of even number using cmd
# Program 19
import sys

# read command line arg excepts the program name
args=sys.argv[1:]

sum=0

for i in args:
    x=int(i)
    if x%2==0:
        sum+=x

print("The sum is :-",sum)