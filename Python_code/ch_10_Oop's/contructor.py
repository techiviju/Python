class Employee():
    name="vijay"
    programming="python"
 
    def __init__(self,name,salary,programming):    # init Dunder method ( means call automatically )
        print("I'm creating an Constructor.")

        self.name=name
        self.salary=salary
        self.programming=programming

    def getInfo(self):
        print(f"Hello {self.name} your detail {self.programming} ")

    @staticmethod
    def greet():
        print("good morning")

vijay=Employee("vijay",12000,"Bash")

print(vijay.name , vijay.salary , vijay.programming)
vijay.getInfo()
vijay.greet()


        # 7 hour 7 min Practice set