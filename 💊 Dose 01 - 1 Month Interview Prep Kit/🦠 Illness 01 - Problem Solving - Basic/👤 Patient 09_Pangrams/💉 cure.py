#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#Solution 1
def pangrams(s):
    # Check if all 26 lowercase letters are present in the input string
    if set(string.ascii_lowercase).issubset(set(s.lower())):
        return 'pangram'  # If yes, return 'pangram'
    else:
        return 'not pangram'  # Otherwise, return 'not pangram'


#Solution 2
def pangrams(s):
    seen = set()  # Set to store unique alphabetic characters found in the string

    for char in s.lower():  # Convert the string to lowercase and iterate over each character
        if char in string.ascii_lowercase:  # Check if the character is a lowercase letter
            seen.add(char)  # Add the character to the set

        if len(seen) == 26:  # If all 26 letters are found, it's a pangram
            return 'pangram'

    return 'not pangram'  # If loop finishes without finding all 26 letters, it's not a pangram

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
