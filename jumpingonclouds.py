#!/bin/python3

import math
import os
import random
import re
import sys

def rec(i, c, n):
    if i == len(c) - 1:
        return n
    if i <= len(c) - 3 and c[i+1] == 0 and c[i+2] == 1:
        return rec(i+1, c, n+1)
    if i <= len(c) - 3 and c[i+1] == 1 and c[i+2] == 0:
        return rec(i+2, c , n+1)
    if i == len(c) - 2 and c[i+1] == 0:
        return rec(i+1, c, n+1)
    return min(rec(i+1, c, n+1), rec(i+2, c , n+1))


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    return rec(0, c, 0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
