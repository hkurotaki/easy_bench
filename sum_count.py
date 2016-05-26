from __future__ import division
import sys
from bench import *

sum_counter, num_counter = sum_count_bench()

print " Key\tTotal\tCount\tEach"
for key, value in sum_counter.items():
    print "%s\t%.10f\t%d\t%.10f" % (key, value, num_counter[key], value / num_counter[key])
