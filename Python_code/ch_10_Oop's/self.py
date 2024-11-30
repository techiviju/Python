class Employee:
    language='python'  # This is a class attribute
    salary=125423

    def getInfo(self):
        print(f"Hello {self.name} The language is {self.language}. The salary is {self.salary} ")

    @staticmethod
    def greet():
        print("Good Morning")

vijay=Employee()
vijay.language="Bash"
vijay.name="vijay"

vijay.getInfo()
# Employee.getInfo(vijay)  # both are same work...

vijay.greet()   # using static method...