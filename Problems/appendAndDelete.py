#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#
def appendAndDelete(s, t, k):
    common_length = 0
    min_length = min(len(s), len(t))
    
    for i in range(min_length):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    total_operations = (len(s) - common_length) + (len(t) - common_length)

    if total_operations > k:
        return "No"
    elif (k - total_operations) % 2 == 0:
        return "Yes"
    elif len(s) + len(t) <= k:
        return "Yes"
    else:
        return "No"
    
    

if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(f"Result => {result}")