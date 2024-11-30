class Company:
    comp="Microsoft"        # class attribute
    def detail(self):
        print(f"Welcome to the {self.comp}")

class Employee:
    name="Vijay"
    def emplo_detail(self):
        print(f"Employee name is {self.name}")

class Programmer(Company,Employee):  # multiple inheritance
    lang="Python"
    def pro(self):
         print(f"My skill is {self.lang}")

vijay=Programmer()
vijay.name="shreyash"   # Instance Attribute
vijay.lang="Bash script" 

ajay=Programmer()

vijay.detail()
vijay.emplo_detail()
vijay.pro()

ajay.name="AJAY"
ajay.emplo_detail()