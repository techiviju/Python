marks={
      'vijay':95,
      'kunal':85,
      3:'arun'
}

# print(marks.items()) #  view object with key-value pairs as tuples
# print(marks.keys())

# print(marks.values()) # displays a list of all the values in the dictionary.

# marks.update({'vijay':94,'hemant':97}) # update the values and use to add

# print(marks.get('vijay2')) # return a value when key is not present then retuen none.
# but in marks.['vijay2'] returns an error.thats a difference.

# print(marks.pop(3,'not fount')) # Removes the specified key and returns its value. If the key is not found, it returns the default value

# last_i=marks.popitem() # It removes the most recently added key-value pair
# If the dictionary is empty, it raises a KeyError.


# marks.clear() # remove all element from the dict

# new_m=marks.copy() # copy the dict

# age=marks.setdefault('age',25) 
# If the key is in the dictionary, it returns the value. If not, it inserts the key with a default value.
