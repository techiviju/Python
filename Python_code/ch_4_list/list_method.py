frd=["vijay",343,'mangesh','kunal',21.02,'hemant','bhushan']

print(frd)
frd.append('Shreyash')  #add name in the end,  Adds a single element to the end of the list.
frd.extend(['Rohit','pavan']) # similar to the append but Adds multiple elements to the end of the list.

print(frd)

l1=[1,2,6,8,5,4,35,21,10,65,21]
# l1.sort()         #sort in increasing order
# l1.reverse()      #reverse all list
# l1.insert(3,333)  # insert 333 in index 3

# l1.pop(3) # in index nu 3 is deleted

# l1.remove(21) # Remove 21 from the list
# l1.extend([11,22])  # similar to the append but Adds multiple elements to the end of the list.

# index=l1.index(10) #Returns the index of the first occurrence of a specified item.
# print(index)

count=l1.count(21) # Returns the number of times a specified item appears in the list.
print(count)