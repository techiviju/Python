# Tuples are faster than lists when working with a fixed-size collection of items
# Most Important Tuple Methods: count(), index(), and unpacking.

tpl=(1,3,6,3,'Bhushan',5,7,'kunal')
no=tpl.count(3)
print(no)

print("index",tpl.index('Bhushan'))

# repeate=tpl*2
# print(repeate)

#in and not in operators: Used to check if an element exists in a tuple.
# print("In :",3 in tpl) # this value is present in the tpl then true
# print("Not in :",2 not in tpl) # # this value is not present in the tpl then true

# Concatinate tpl
a=(1,8,44,32,456,85)
concat=tpl+a
print(concat)

# Unpacking
'''
b,c,d,e,f,g=a
print(b) # output 1
'''

# length
print("length",len(tpl))

print("min",min(a))
print("max",max(a))

print("sum",sum(a)) #Returns the sum of all the elements in the tuple (if they are numeric).
