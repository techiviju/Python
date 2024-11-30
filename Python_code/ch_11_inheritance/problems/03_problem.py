class Employee:
    salary=234
    increment=20

    @property
    def salaryAfterIncrenent(self):
        return (self.salary+self.salary*(self.increment/100))
    
    @salaryAfterIncrenent.setter
    def salaryAfterIncrement(self, salary):
        self.increment=((salary/self.salary)-1)*100

e=Employee()
# print(e.salaryAfterIncrement())
print(e.salaryAfterIncrement," print")

e.salaryAfterIncrement = 280.8 
print(e.increment)
