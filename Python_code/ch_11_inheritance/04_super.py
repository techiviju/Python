class Employee:
    def __init__(self):
        print("Employee name is run")
    salary=35

class Programmer(Employee):
    def __init__(self):
        print("programmer is run")
    skill="python"

class Manager(Programmer):
    def __init__(self):
        super().__init__()  # used to run parent constructor...
        print(f"Manager is running {self.salary}")
    s=56


vijay=Manager()
print(vijay.salary)
