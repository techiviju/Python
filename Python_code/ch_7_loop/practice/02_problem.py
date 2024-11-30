# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.

lst=["hemant","himanshu","adi","vijay","harshal","hitesh","dipak"]

for name in lst:
      if(name.startswith("h")):
            print(f"Hello {name}")