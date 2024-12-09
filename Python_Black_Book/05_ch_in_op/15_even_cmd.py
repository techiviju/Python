# find sum of even number using cmd

import sys

args=sys.argv[1:]

sum=0

for i in args:
    x=int(i)
    if x%2==0:
        sum+=x

print("The sum is :-",sum)