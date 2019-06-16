from unittest import TestCase
from series_sum import sum_of_terms


# Test for series sum calculator
class TestSeriesSum(TestCase):

    def test_sum_of_terms(self):

        self.assertEqual(sum_of_terms(2, 1, 2), 3.0)
        