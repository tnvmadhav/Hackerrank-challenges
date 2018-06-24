#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = 0
    max = 0
    flag = 0
    minCount = 0
    maxCount = 0
    myAns = []
    for i in scores:
        if max is 0 and min is 0 and i is not 0 and flag is not 1:
            max = i
            min = i
        if i is 0:
            min = 0
            flag = 1
        elif i < min:
            minCount += 1
            min = i
        elif i > max:
            maxCount += 1
            max = i
    print(max)
    print(min)
    myAns.append(maxCount)
    myAns.append(minCount)
    return myAns
        
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
