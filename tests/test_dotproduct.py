from unittest import TestCase
from dot_product import get_dot_product

# Test(s) for dot product calculator
class TestDotProduct(TestCase):
   
    """ Ensure that the dot product of all vectors 
    at right angles to each other is always zero. """   
    def test_right_angle(self):

        if get_dot_product(90, 15, 18):

            self.assertEqual(get_dot_product(), 0)