# When adding classmethod then print only class attribute.

class Employee:
    a=1
    @classmethod  
    def earning(cls):
         print(f"class attributer is {cls.a}")

e=Employee()
e.a=45
e.earning()