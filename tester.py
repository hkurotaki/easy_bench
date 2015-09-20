import unittest
from bench import *

class TestBench(unittest.TestCase):
    def test_class_style(self):
        with Bench("bench1"):
            pass
    
    def test_function_style(self):
        with bench("bench1"):
            pass
        
    def test_sum(self):
        sum_bench()

if __name__ == '__main__':
    unittest.main()
