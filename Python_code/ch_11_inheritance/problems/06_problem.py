class Vector:
    def __init__(self,r,s,t):
        self.r=r
        self.s=s
        self.t=t

    def __add__(self,other):
        result=Vector(self.r+other.r,self.s+other.s,self.t+other.t)
        return result
    
    def __mul__(self,other):
        result=self.r*other.r+self.s*other.s+self.t*other.t
        return result
    
    def __str__(self):
        return f"{self.r}i , {self.s}j , {self.t}k"
    
v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=Vector(7,8,9)

print(v1+v2)
print(v1*v2)

print(v1+v3)
print(v1*v3)