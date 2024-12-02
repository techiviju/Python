# same as a bytes but bytearray can be modifoed

element=[2,5,0,255,2]

b=bytearray(element)

for i in b:
    print(i)

b[1]=10

print("midified :-",b[1])