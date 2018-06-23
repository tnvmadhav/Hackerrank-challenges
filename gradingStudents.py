#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    list = []
    for i in grades:
        if i >= 38:
            if i%5 > 2:
                ans = i + (5 - (i%5))
            else:
                ans = i
            list.append(ans)
        else:
            list.append(i)
    return list    
                

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
