#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

#Solution 1
def flippingBits(n):
    # Step 1: Convert to binary manually
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    # Pad to 32 bits manually
    while len(binary) < 32:
        binary = '0' + binary

    # Step 2: Flip the bits
    flipped_binary = ""
    for bit in binary:
        if bit == '0':
            flipped_binary += '1'
        else:
            flipped_binary += '0'

    # Step 3: Convert flipped binary to decimal
    decimal = 0
    power = 0
    for i in range(len(flipped_binary) - 1, -1, -1):
        decimal += int(flipped_binary[i]) * (2 ** power)
        power += 1

    return decimal

#Soltion 2
def flippingBits(n):
    # Convert to 32-bit binary string
    binary = bin(n)[2:].zfill(32)  # Strip '0b', then pad with leading zeros

    # Flip the bits using one-liner
    flipped = ''.join('1' if bit == '0' else '0' for bit in binary)

    # Convert back to decimal
    return int(flipped, 2)  # Convert binary string to integer

#Solution 3
def flippingBits(n):
    # XOR with 32-bit all 1s (i.e., 0xFFFFFFFF or 4294967295)
    return n ^ 0xFFFFFFFF  # Flips all bits in a 32-bit number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
