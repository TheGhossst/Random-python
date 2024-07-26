#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

'''
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.
'''
def repeatedString(s, n):
    count_a_in_s = s.count('a')
    len_s = len(s)
    complete_repeats = n // len_s
    total_count_a = complete_repeats * count_a_in_s
    remaining_chars = n % len_s
    total_count_a += s[:remaining_chars].count('a')
    
    return total_count_a
    
    
if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(f"Result -> {result}")
