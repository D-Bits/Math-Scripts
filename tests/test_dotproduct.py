from unittest import TestCase
from dot_product import get_dot_product

# Test(s) for dot product calculator
class TestDotProduct(TestCase):
   
    """ Ensure that the dot product of two vectors 
    at right angles to each other is always zero. """   
    def test_right_angle(self):

        self.assertAlmostEqual(get_dot_product(90, 15, 18), 0)

    """ Test that the dot product of two vectors at 
    angles between 90 and 180 degrees are always
    negative  """
    def test_90_or_180(self):

        self.assertLess(get_dot_product(120, 12, 20), 0)
        self.assertLess(get_dot_product(152, 34, 28), 0)