# This program calculates the sum of all elements in a list using recursion.

def sum_list(lst):
    if not lst:  # Base case: if the list is empty
        return 0
    else:
        return lst[0] + sum_list(lst[1:])  # Recursive case

print(sum_list([1, 2, 3, 4, 5])) 