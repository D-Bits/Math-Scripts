from vectors import get_dot_product
from series import get_fibonacci, get_num_of_fib, sum_of_terms
from math import factorial

# Choices for the user
options = {
    '1': 'Calculate the dot product of two vectors.',
    '2': 'Get the sum of the first n terms in an arithmetic series.',
    '3': 'Get a specific number in the Fibonacci sequence.',
    '4': 'Output the first n numbers in the Fibonacci sequence.',
    '5': 'Calculate a factorial.'
}


if __name__ == "__main__":
    
    print() # Blank line for readability

    # Show the user their choices
    for key, val in options.items():
        
        print(key, val)

    print() # Blank line for readability
    choice = int(input('Enter a choice, based on the above options: '))
    print()

    if choice == 1:
        vec_angle = float(input('Enter the angle between the two vectors (in degrees): '))
        vec_a = int(input('Enter the magnitude of the first vector: '))
        vec_b = int(input('Enter the magnitude of the second vector: '))
        print('The dot product is:', get_dot_product(vec_angle, vec_a, vec_b), "\n")
    elif choice == 2:
        num_of_terms = int(input('Enter the number of terms in the series: '))
        first_term = int(input('Enter the first term in the series: '))
        second_term = int(input('Enter the second term in the series: '))
        print(f'The sum of the first {num_of_terms} terms in the series is:', sum_of_terms(num_of_terms, first_term, second_term), "\n")
    elif choice == 3:
        fib_numb = int(input('Enter which number in the Fibonacci sequence you want to get the value of: '))
        print(f'The {fib_numb} number in the Fibonacci sequence is:', get_fibonacci(fib_numb))
    elif choice == 4:
        fib_terms = int(input('Enter a number of terms in the Fibonacci sequence to display: '))
        print(get_num_of_fib(fib_terms))
    else:
        raise Exception('Invalid Input.')