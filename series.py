"""
Various functions involving arithmetic series.
"""

# Get the nth term in the Fibonacci sequence
def get_fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (get_fibonacci(n-1) + get_fibonacci(n-2))


# Get the first n terms in the Fibonacci sequence
def get_num_of_fib(fib_nums):

    for n in range(1, fib_nums + 1):
    
        print(n, ":", get_fibonacci(n))


# Find the sum the first n terms in a arithmetic series. 
def sum_of_terms(n , a1, a2):

    sum_add = a1 + a2
    series_sum = n * sum_add / 2

    return series_sum