class programmer:
    company="microsoft"

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        # print(self.company,name,salary,pin)

p=programmer("vijay",12000,442865)
print(p.company,p.name,p.salary,p.pin)
s=programmer("shreyash",123000,445566)
print(s.company,s.name,s.salary,s.pin)