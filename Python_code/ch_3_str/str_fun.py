name='vijay'
print(len(name)) # 5
print(name.endswith('ay')) # return true
print(name.startswith('vi')) #true

# print(name.capitalize()) # capital only First word
'''
nu=list(range(1,10))
print(nu)

title=name.title()
print("title :",title)

print("find :",name.find('ja')) # show the index number

num=-50
print('abs fun :',abs(num)) #returns the absolute value of a number, which means it converts negative numbers to positive.
print(abs(32))  # print positive value
print(abs(12*(-5)))
'''
# print(max(20))

name="  hello vijay "
print(name.strip()) #remove leading and tralling spaces.
print(name.upper())
print(name.lower())

print(name.count('a')) #Returns the number of non-overlapping occurrences of a substring in the string

latter='this'
print(latter.isalpha()) # if all characters in the string are alphabetic > true

latter2='12345'
print(latter2.isdigit())

latter3="checkalphaandnu1235"
print(latter3.isalnum())