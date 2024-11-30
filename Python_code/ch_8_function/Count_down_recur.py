def countdown(n):
    if n < 0:  # Base case: if n is negative
        return
    else:
        print(n)  # Print the current number
        countdown(n - 1)  # Recursive case


countdown(5)
