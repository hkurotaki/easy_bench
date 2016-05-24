import sys
from bench import *

sum_counter, num_counter = sum_count_bench()
for key, value in sum_counter.items():
    print key, value, num_counter[key]
