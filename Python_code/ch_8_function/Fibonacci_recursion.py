def fibonacci(n):
    if n <= 0:  # Base case: if n is 0 or negative, return an empty list
        return []
    elif n == 1:  # Base case: if n is 1, return a list with the first Fibonacci number
        return [0]
    elif n == 2:  # Base case: if n is 2, return the first two Fibonacci numbers
        return [0, 1]
    else:
        # Recursive case: get the Fibonacci series for n-1
        series = fibonacci(n - 1)
        # Append the next Fibonacci number to the series
        next_fib = series[-1] + series[-2]  # Sum of the last two numbers
        series.append(next_fib)
        return series

# Get user input
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Generate and print the Fibonacci series
fib_series = fibonacci(num_terms)
print("Fibonacci series:", fib_series)
