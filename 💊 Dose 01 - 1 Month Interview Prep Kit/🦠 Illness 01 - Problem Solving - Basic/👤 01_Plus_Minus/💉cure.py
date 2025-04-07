#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Calculate the proportion of positive numbers
    positive_count = sum(1 for x in arr if x > 0) / len(arr)
    
    # Calculate the proportion of negative numbers
    negative_count = sum(1 for x in arr if x < 0) / len(arr)
    
    # Calculate the proportion of zeros
    zero_count = sum(1 for x in arr if x == 0) / len(arr)
    
    # Store all results formatted to 6 decimal places in a list
    output_array = [
        f"{positive_count:.6f}",
        f"{negative_count:.6f}",
        f"{zero_count:.6f}"
    ]
    
    # Print each value on a new line
    for num in output_array:
        print(num)

if __name__ == '__main__':
    # Read the number of elements (not strictly needed since we use len(arr))
    n = int(input().strip())

    # Read the array as space-separated integers
    arr = list(map(int, input().rstrip().split()))

    # Call the function
    plusMinus(arr)
