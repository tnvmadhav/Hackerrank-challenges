#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    flag = 0
    iflag = 0
    oflag=  0
    count = 0
    limit =0
    a = sorted(a)
    large = max(a)
    b= sorted(b)
    for x in b:
        if x >=large:
            limit = x
            break  
    for i in range(large,limit+1):
        oflag=0
        iflag=0
        flag=0
        for k in a:
            if i%k != 0:
                iflag = 1
                break
        if iflag is 0:
            if limit%i is 0:
                flag = 1
                print(i)
                if flag is 1:
                    for j in b:
                        if j%i != 0:
                            oflag = 1
                            break
                    if oflag is 0:
                        count +=1
    if limit is 0:
        return 0
    else :
        return count    
            
            
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

