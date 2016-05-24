"""
A benchmark utility to measure running time.

Usage:
    
    with Bench("test_category"):
        blah
        blah
        
    or
        
    trace = Bench("test_category")
    blah
    blah
    trace.end()
    
    or 
    
    with bench("test_category"):
        blah
        blah
"""
__author__ = "napman <kotaro.nakayama@gmail.com>"

import sys
import collections
import time, random

DEFAULT_LOGFILE = "benchmark.log"

# time benchmark 
class Bench():
    def __init__(self, key=""):
        if not 'benchmark_log_file' in globals():
            Bench.init_benchmark(DEFAULT_LOGFILE)
        
        self.key = key
        self.hash_key = random.getrandbits(128)
        self.start_time = time.time()
        
    @staticmethod
    def init_benchmark(log_file):
        global benchmark_log_file
        benchmark_log_file = open(log_file, "w", 0) # buffer 0 to write immediately
    
    def get_span(self):
       end_time = time.time()
       time_spent = end_time - self.start_time
       return time_spent
    
    def end(self):
        global benchmark_log_file
        time_spent = self.get_span()
        #benchmark_log_file.write("%s\t%f\n" % (self.key, time_spent))
	benchmark_log_file.write("%s\t%.10f\n" % (self.key, time_spent))
        return time_spent
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.end()

def set_logfile(log_file=DEFAULT_LOGFILE):
    Bench.init_benchmark(log_file)

def bench(key):
    return Bench(key)

def sum_bench(benchmark_file=DEFAULT_LOGFILE):
    counter = collections.Counter()
    with open(benchmark_file, 'r') as fp:
        lines = [line.split("\t") for line in fp.read().splitlines()]
        for line in lines:
            counter[line[0]] += float(line[1])
            
    return counter

def sum_count_bench(benchmark_file=DEFAULT_LOGFILE):
    sum_counter = collections.Counter()
    num_counter = collections.Counter()
    with open(benchmark_file, 'r') as fp:
        lines = [line.split("\t") for line in fp.read().splitlines()]
        for line in lines:
            sum_counter[line[0]] += float(line[1])
            num_counter[line[0]] += 1
            
    return sum_counter, num_counter
