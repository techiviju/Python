# Inheritance in Python is like a way for one class (think of it as a blueprint for making things)
# to use the features of another class. Imagine you have a toy called "Animal," and you want to 
# make a special toy called "Dog." Instead of starting from scratch, the "Dog" can inherit the 
# traits of the "Animal."class Employee:

#  inheritance helps us create new classes that share features with existing ones, making it easier to organize and reuse code!

# In single inheritance, a class (child) inherits from one other class (parent).


class Animal:
    def sound(self):
        # return "i make a sound"
        print(f"i make a sound this is animal class {self.kill}")
    
class Dog(Animal):
    def bark(self):
        return "I'm Barking"
    
me_animal=Dog()
me_animal.kill="dhudhu"
me_animal.sound()
print(me_animal.bark())

# __pycache
# Antrostone