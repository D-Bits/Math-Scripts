"""
Functions to do various calculations involving vectors.
"""
from math import cos, pi, radians


# Get the dot product of two vectors
def get_dot_product(angle, vector_a, vector_b):

    # Convert degrees (from angle input) to radians
    rad_conversion = radians(angle)

    # Calculate the dot product, based on obtained values
    dot_product = vector_a * vector_b * cos(rad_conversion)

    return round(dot_product, 2)
