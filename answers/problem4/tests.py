import unittest
from answer import search
import math
import random

class Testing(unittest.TestCase):
    def testing_search(self):
        testing_array = [3, 4, -1, 1]
        expected_results = 2

        actual_results = search(testing_array)

        self.assertEquals(expected_results, actual_results)
    
    
    def testing_search1(self):
        testing_array = [1, 2, 0]
        expected_results = 3

        actual_results = search(testing_array)

        self.assertEquals(expected_results, actual_results)
    
    
    def testing_search3(self):
        testing_array = [-1, 0, 3, 4]
        expected_results = 1

        actual_results = search(testing_array)

        self.assertEquals(expected_results, actual_results)
    
    
    def testing_search2(self):
        answer = math.floor(random.randrange(1, 10000))

        testing_array = [x for x in range(0, 20000)]
        expected_results = answer
        del testing_array[answer]

        actual_results = search(testing_array)

        self.assertEquals(expected_results, actual_results)
    
    
    def testing_search5(self):
        answer = math.floor(random.randrange(1, 100))
        new_number1 = math.floor(random.randrange(answer + 1, 100))
        new_number2 = math.floor(random.randrange(answer + 1, 100))
        new_number3 = math.floor(random.randrange(answer + 1, 100))
        new_number4 = math.floor(random.randrange(answer + 1, 100))

        testing_array = [x for x in range(-1000, 100)]

        del testing_array[int(answer) + 1000]
        del testing_array[new_number1]
        del testing_array[new_number2]
        del testing_array[new_number3]
        del testing_array[new_number4]
        actual_results = search(testing_array)

        self.assertEquals(answer, actual_results)
    

    def testing_search4(self):
        testing_array = [1, 3, 2, 5, 6, 1, 2]
        expected_results = 4

        actual_results = search(testing_array)

        self.assertEquals(expected_results, actual_results)