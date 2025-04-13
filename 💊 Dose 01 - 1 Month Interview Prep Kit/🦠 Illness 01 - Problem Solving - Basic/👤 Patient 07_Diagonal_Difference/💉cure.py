#!/bin/python3

import math
import os
import random
import re
import sys

#Solution 1
# Function to compute the absolute difference between the sums of the diagonals of a square matrix
def diagonalDifference(arr):
    diag1 = 0  # To store the sum of the primary diagonal (top-left to bottom-right)
    diag2 = 0  # To store the sum of the secondary diagonal (top-right to bottom-left)
    index = len(arr)  # Number of rows/columns in the square matrix

    # Loop through each row of the matrix
   for i in range(len(arr)):
        for j in range(len(arr)):
            # Primary diagonal element is where row index == column index
            if (i == j):
                diag1 += arr[i][j]

         # Decrement the index to get the corresponding column for secondary diagonal
        index = index - 1
        diag2 += arr[i][index]

    # Calculate the absolute difference between the two diagonals
    result = abs(diag1 - diag2)

    return result

#Solution 2
def diagonalDifference(arr):
    diag1 = 0  # Sum of primary diagonal
    diag2 = 0  # Sum of secondary diagonal
    n = len(arr)

    for i in range(n):
        diag1 += arr[i][i]           # Primary diagonal element
        diag2 += arr[i][n - 1 - i]   # Secondary diagonal element

    return abs(diag1 - diag2)

if __name__ == '__main__':
    # Open a file to write the output (environment variable OUTPUT_PATH must be set)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the size of the matrix
    n = int(input().strip())

    arr = []  # Initialize the 2D list (matrix)

    # Read each row of the matrix
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Compute the result using the function
    result = diagonalDifference(arr)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the file
    fptr.close()
