# 4. Add a static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print("square :",self.n*self.n)
    
    def cube(self):
        print("Cube :",self.n*self.n*self.n)

    def s_root(self):
        print("square root :",self.n**1/2)

    @staticmethod
    def greet():
        print("Calculation is Done Good job..")

calc=calculator(5)

calc.square()
calc.cube()
calc.s_root()

calc.greet()