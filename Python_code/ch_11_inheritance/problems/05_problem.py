class Vector:
    def __init__(self,r,s,t):
        self.r=r  #  store these values in the object.  
        self.s=s
        self.t=t
        
    def __add__(self,other):
        # This method allows you to add two vectors using the + operator.
        result=Vector(self.r+other.r,self.s+other.s,self.t+other.t)
        return result
#     It creates a new Vector object where each component is the sum of the corresponding components of the two vectors.
#     For example, if you add v1 and v2, it adds v1.r to v2.r, v1.s to v2.s, and v1.t to v2.t.
        
    def __mul__(self,other):
        result=(self.r*other.r+self.s*other.s+self.t*other.t)
        return result
    
    # This method defines how to represent the vector as a string.
    def __str__(self):
        return f"Vector({self.r},{self.s},{self.t})"
    # When you print a vector object, it will show its components in a readable format.
    
v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=Vector(7,8,9)

print(v1+v2)
print(v1*v2)

print(v1+v3)
print(v1*v3)