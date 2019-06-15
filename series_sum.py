"""
Find the sum the first n terms in a series.  
"""


def get_sum_of_terms():

    n = int(input('Enter the number of terms in the series: '))
    a1 = int(input('Enter the first term in the series: '))
    a2 = int(input('Enter the second term in the series: '))

    # Calculate the sum of the series
    sum_add = a1 + a2
    series_sum = n * sum_add / 2

    return series_sum
   