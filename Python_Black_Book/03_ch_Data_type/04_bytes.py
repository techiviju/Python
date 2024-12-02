# Cannot modify
# Byte Array Range form 0 to 256

element=[10,15,14,5,14,255,0]

b=bytes(element)
print("0th element :- ",b[0])
for i in b:
    print(i)