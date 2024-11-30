class Employee:
    a=1
    @classmethod
    def showe(cls):
        print(f"class attribute value is  {cls.a}")

    @property  #allows you to manage the attributes of a class in a more controlled way.
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=Employee()
e.a=45          # instance attribute
e.showe()

e.name="vijay chaudhari"
print(e.fname, e.lname)


# @property is built-in function that allows you to define methods in a class that can be accessed like attributes.
# It helps in encapsulating data and controlling access to class attributes.