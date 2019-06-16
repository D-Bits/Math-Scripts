from math import cos, pi, radians

""" 
Get the dot product of two vectors, based on user input.
1. Get the angle between the two vectors.
2. Get the magnitude of the first vector.
3. Get the magnitude of the second vector.
4. Convert degrees to radians.
5. Multiply the magnitudes 
"""


# Get appropriate values from user for calculations
def user_input_dot_product():

    angle = float(input('Enter the angle between the two vectors (in degrees): '))
    vector_a = int(input('Enter the magnitude of the first vector: '))
    vector_b = int(input('Enter the magnitude of the second vector: '))

    # Convert degrees (from angle input) to radians
    rad_conversion = radians(angle)

    # Calculate the dot product, based on obtained values
    dot_product = vector_a * vector_b * cos(rad_conversion)

    # Round off the dot product to 2 digits
    rounded = round(dot_product, 2)

    print('The dot product is:', rounded)


""" Create a parameterized version of the above 
function, for unit testing purposes """
def get_dot_product(angle, vector_a, vector_b):

    # Convert degrees (from angle input) to radians
    rad_conversion = radians(angle)

    # Calculate the dot product, based on obtained values
    dot_product = vector_a * vector_b * cos(rad_conversion)

    return round(dot_product, 2)