#  to find square of a given number

import argparse

# create ArgumentParser class obj
parser=argparse.ArgumentParser(description="This program display the square value of given nu")

# add one argument with name num and type as int
parser.add_argument("num",type=int,help="please enter input integer type number")

# retrive the arguments passed to the program
args=parser.parse_args()

# find the square of the argument passed
result=args.num**2

print("square value is :-",result)