class Employee:
    a=1

class sec_chi(Employee):
    b=2

class last_child(sec_chi):
    c=3

o=Employee()
print(o.a)      # print a value 
# print(o.b)      # not printed because not present in there.

o=last_child()      # Print Everything because present inhet all classes
print(o.a,o.b,o.c)