class Employee:
    language='python'  # This is a class attribute
    salary=125423

vijay=Employee()   # object
vijay.name='VIJAY'   # This is an instance attribute.
print(vijay.name,vijay.language,vijay.salary)

shreyash=Employee()     # object
shreyash.name='Shreyash'
print(shreyash.name,shreyash.salary,shreyash.language)