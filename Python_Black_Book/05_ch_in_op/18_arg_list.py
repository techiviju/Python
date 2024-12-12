# Find power value of a number

import argparse

parser=argparse.ArgumentParser()

parser.add_argument('nums',nargs='+')

# retrive the argument into args obj
args=parser.parse_args()

# display the arguments from the list
for x in args.nums:
    print(x)