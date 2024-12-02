# same as a bytes but bytearray can be modifoed

element=[2,5,0,255,2]

b=bytearray(element)

for i in b:
    print(i)

b[1]=10

print("midified :-",b[1])

# you can do with tuple also

e=(5,6,5,8)

e2=bytearray(e)
print(" e ",e[0])

print("type of e ",type(e2))

print("type of e ",type(b))