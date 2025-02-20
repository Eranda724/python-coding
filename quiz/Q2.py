#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts STRING s as parameter.
#

def solve(s):
    # Write your code here
    words = s.split()
    words.sort()
    total = 0
    for word in words:
        word = word.lower()
        total += ord(word[0]) - ord('a') + 1
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                total += ord(word[i]) - ord('a') + 1
                break


    return round(total / len(words), 2)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = solve(s)

        fptr.write(str(result) + '\n')

    fptr.close()
