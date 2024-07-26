#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY crew_id
#  2. INTEGER_ARRAY job_id
#

def getMinCost(crew_id, job_id):
    a = sorted(crew_id)
    b = sorted(job_id)
    min_dist = 0
    
    for i in range(len(a)):
        min_dist += abs(a[i] - b[i])
        
    return min_dist

if __name__ == '__main__':
    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)

    print(f"Result -> {result}")
