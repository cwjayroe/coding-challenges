import unittest
from answer import number_array_multiplier

class Testing(unittest.TestCase):
    def test_number_array_multiplier1(self):
        test_array = [1, 2, 3, 4, 5]
        expected_results = [120, 60, 40, 30, 24]

        actual_results = number_array_multiplier(test_array)

        self.assertEquals(expected_results, actual_results)
    
    
    def test_number_array_multiplier2(self):
        test_array = [4, 3, 2, 1]
        expected_results = [6, 8, 12, 24]

        actual_results = number_array_multiplier(test_array)

        self.assertEquals(expected_results, actual_results)