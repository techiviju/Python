# Write a class “Calculator” capable of finding square, cube and square root of a number

class calculator:

    # def __init__(self,number):
    #     print("Square :",number*number)

    #     print("cube is :",number*number*number)

    #     print("square root :",number**1/2)

            #  OR................

    def __init__(self,n):
        self.n=n

    def cube(self):
        print("Cube is:",self.n*self.n*self.n)

    def square(self):
        print("square is:",self.n*self.n)

    def square_root(self):
        print("Square root is:",self.n**1/2)
    

calc=calculator(5)

calc.cube()
calc.square()
calc.square_root()