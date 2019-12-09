import unittest
from answer import check_if_matches

class Testing(unittest.TestCase):
    def test_check_if_matches1(self):
        test_array = [10,15,3,7]
        test_k = 17

        expected_results = True
        actual_results = check_if_matches(test_array, test_k)
        self.assertEqual(expected_results, actual_results)
    
    
    def test_check_if_matches2(self):
        test_array = [5,8,10]
        test_k = 18

        expected_results = True
        actual_results = check_if_matches(test_array, test_k)
        self.assertEqual(expected_results, actual_results)
    
    
    def test_check_if_matches3(self):
        test_array = [5,8,12]
        test_k = 18

        expected_results = False
        actual_results = check_if_matches(test_array, test_k)
        self.assertEqual(expected_results, actual_results)