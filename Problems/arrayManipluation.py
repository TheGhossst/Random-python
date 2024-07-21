#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    diff = [0] * n
    
    for left, right, val in queries:
        print(f"left -> {left}")
        print(f"right -> {right}")
        print(f"val -> {val}")
        diff[left - 1] += val
        if right < n:
            diff[right] -= val
        print(f"diff -> {diff}")
    print("\n")
    max_value = 0
    current_value = 0
    for i in range(n):
        print(f"diff[i] -> {diff[i]}")
        current_value += diff[i]
        if current_value > max_value:
            max_value = current_value
        print(f"current_value -> {current_value}")
        print(f"max_value -> {max_value}")
        print("\n")
        
    return max_value
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')