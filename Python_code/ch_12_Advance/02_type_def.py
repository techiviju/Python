# TYPES DEFINITIONS IN PYTHON
from typing import List,Tuple,Union,Dict
n:int=10

name : str ="vijay"

def sum(a:int,b:int)->int:
    return a+b


# types

num: List[int]=[1,2,3,4,5]

person: Tuple[str, int] = ("Alice", 30)

scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

print(num,type(num))

# Union type for variables that can hold multiple types

identifier: Union[int, str] = "ID123"
# identifier = 12345 # Also valid

print(identifier,type(identifier))