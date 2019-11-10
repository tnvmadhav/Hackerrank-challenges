#!/bin/python3

import math
import os
import random
import re
import sys


def freq(s):
    count = 0
    for i in s:
        if i == 'a':
            count+=1
    return count

# Complete the repeatedString function below.
def repeatedString(s, n):
    return (int(n/len(s)) * freq(s)) + freq(s[:n%len(s)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
