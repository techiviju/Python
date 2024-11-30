    # Problem 1
'''
name=input("Enter your name:-")
#print("Hello %s Good afternoon"%name)
print(f"Good afternoon {name}")
'''

# Write program to fill in a latter template given below with name and date.

latter=''' Dear <|Name|>,
           your selected!
           <|Date|>
           '''
#print(latter.replace('<|Name|>',"vijay").replace('<|Date|>','08/cot/2024')) #chaning


# Write a program to detect double space in a string.
'''
name='vijay is a good  programmer and he is so talented'
print(name.find("  "))
'''

#replace the double from the program ^ with single space.
name='vijay is a good  programmer and he so talented'
print(name.find('ted'))
print(name.replace("  "," ")) # string are immutable
print(name.replace("  "," ").find('ted'))


# print(name.find('ted'))
