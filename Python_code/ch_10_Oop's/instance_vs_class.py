class Employee:
    language='python'  # This is a class attribute
    salary=125423

vijay=Employee()
vijay.language='javascript'   # This is an instance attribute.
print(vijay.language,vijay.salary)