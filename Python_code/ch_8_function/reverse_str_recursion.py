def reverse_string(s):
    if len(s) == 0:  # Base case: if the string is empty
        return s
    else:
        return s[-1] + reverse_string(s[:-1])  # Recursive case

# Example usage
print(reverse_string("vijay"))
