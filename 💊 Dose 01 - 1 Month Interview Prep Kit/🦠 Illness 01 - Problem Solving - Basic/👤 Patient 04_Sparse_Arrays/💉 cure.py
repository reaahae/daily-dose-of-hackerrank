#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


def matchingStrings(strings, queries):
    # Count the frequency of each string in the 'strings' list
    string_counter = Counter(strings)
    
    # For each query, retrieve its count from the string_counter
    # If a query is not found, Counter will return 0 by default
    result = [string_counter[x] for x in queries]
    
    # Return the list of counts corresponding to each query
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
