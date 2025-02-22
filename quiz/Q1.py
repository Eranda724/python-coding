#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def longestCommonSubsequence(a, b):
    n, m = len(a), len(b)

    #k = [[0] * (m + 1) for _ in range(n + 1)]
    k = []
    for i in range(n + 1):
        k.append([0] * (m + 1))

    k[0][0] = 0
    
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                k[i][j] = k[i - 1][j - 1] + 1
            else:
                k[i][j] = max(k[i - 1][j], k[i][j - 1])

    i, j = n, m
    p = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            p.append(a[i - 1])
            i -= 1
            j -= 1
        elif k[i - 1][j] > k[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return p[::-1] 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
