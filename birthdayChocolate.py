#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s, d, m):
    count = 0
    for i in range(len(s)-m+1):
        count += (sum(s[i:i+m]) == d)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
