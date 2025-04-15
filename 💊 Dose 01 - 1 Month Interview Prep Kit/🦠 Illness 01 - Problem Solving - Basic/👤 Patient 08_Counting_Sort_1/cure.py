#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr): 
    # Initialize a list of 100 zeros to store the frequency of each number from 0 to 99
    result = [0] * 100
    
    # Iterate through each element in the input array
    for i in arr:
        # Increment the count at the index corresponding to the number
        result[i] += 1
    
    # Return the frequency array
    return result  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
