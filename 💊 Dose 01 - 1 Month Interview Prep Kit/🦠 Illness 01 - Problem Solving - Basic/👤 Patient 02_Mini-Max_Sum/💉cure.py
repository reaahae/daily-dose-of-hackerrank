#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

#Solution 1
def miniMaxSum(arr):
    # Sort the array in ascending order
    sorted_arr = sorted(arr)
    
    # Calculate the sum of the first 4 elements (smallest values)
    min_sum = sum(sorted_arr[:4])
    
    # Calculate the sum of the last 4 elements (largest values)
    max_sum = sum(sorted_arr[-4:])
    
    # Print the minimum and maximum sums
    print(min_sum, max_sum)

#Solution 2
def miniMaxSum(arr):
    # Calculate the total sum of all elements in the array
    total = sum(arr)
    
    # To get the minimum sum, subtract the maximum element from the total
    # (i.e., the sum of the other 4 smallest elements)
    min_sum = total - max(arr)
    
    # To get the maximum sum, subtract the minimum element from the total
    # (i.e., the sum of the other 4 largest elements)
    max_sum = total - min(arr)
    
    # Print the minimum and maximum sums
    print(min_sum, max_sum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

