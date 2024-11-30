# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class atrri:
    a=4        # class attributes.

c=atrri()
print(c.a)  # Prints the class attribute because instance attribute is not present

c.a=0        # Instance attribute is set
print(c.a)   # Prints the instance attribute because instance attribute is present

print(atrri.a)   # Prints the class attribute
