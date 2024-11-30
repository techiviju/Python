class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"Two D value is :-{self.i} & {self.j}")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show3(self):
        print(f"three D vector is {self.i} {self.j} {self.k}")

t=TwoDvector(1,2)
t.show()

a=ThreeDvector(2,3,5)
a.show3()