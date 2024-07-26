#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'nearlySimilarRectangles' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_LONG_INTEGER_ARRAY sides as parameter.
#

def nearlySimilarRectangles(sides):
    res = 0
    ratio_map = {}
    
    for side in sides:
        ratio = side[0] * 100000 // side[1]
        if ratio in ratio_map:
            ratio_map[ratio] += 1
        else:
            ratio_map[ratio] = 1
    
    for count in ratio_map.values():
        if count > 1:
            res += (count * (count - 1)) // 2
    
    return res

if __name__ == '__main__':

    sides_rows = int(input().strip())
    sides_columns = int(input().strip())

    sides = []

    for _ in range(sides_rows):
        sides.append(list(map(int, input().rstrip().split())))

    result = nearlySimilarRectangles(sides)

    print(f"Result -> {result}")
