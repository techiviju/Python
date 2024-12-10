# add two num using argument parser

import argparse

parser=argparse.ArgumentParser(description="This program is accept the float value and display addition")

parser.add_argument("n1",type=float,help="Enter float value")

parser.add_argument("n2",type=float,help="Enter float value")

args=parser.parse_args()

result=float(args.n1)+float(args.n2)

print("the add is :-",result)