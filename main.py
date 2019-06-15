from dot_product import get_dot_product
from series_sum import get_sum_of_terms

# Choices for the user
options = {
    '1': 'Calculate the dot product of two vectors.',
    '2': 'Get the sum of the first n terms in an arithmetic series.'
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
        get_dot_product()
    elif choice == 2:
        get_sum_of_terms()
    else:
        raise Exception('Invalid Input.')