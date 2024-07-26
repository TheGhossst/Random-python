#!/bin/python3
#https://www.hackerrank.com/challenges/fibonacci-modified/problem

import math
import os
import random
import re
import sys

sys.set_int_max_str_digits(1000000)  #Wont work otherwise
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n): #O(n)
    d = {1: t1, 2: t2}
    for i in range(3, n+1):
        d[i] = d[i - 2] + (d[i - 1] * d[i - 1])
    return d[n]
    
'''def fibonacciModified(t1, t2, n):''
    dp = [None] * (n + 1)
    
    dp[1] = t1
    dp[2] = t2

    def fib(n):
        if dp[n] is not None:
            return dp[n]
        dp[n] = fib(n - 2) + (fib(n - 1) * fib(n - 1))
        return dp[n]
    
    return fib(n)'''
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    print(f"Result -> {result}")
