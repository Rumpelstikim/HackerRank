# Given an integer, n, perform the following conditional actions:
# Si n is odd, print Weird
# Si n even and in the inclusive range of  2 to 5, print Not Weird
# If is even and in the inclusive range of 6 to 20, print Weird
# If is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not is weird.

import math
import os
import random
import re
import sys

def es_par():
    if N % 2 != 0:
        print("Weird")
    else:
        if N in range(2,5):
            print("Not Weird")
        if N in range (6,20):
            print("Weird")
        if N > 20:
            print("Not Weird")

if __name__ == '__main__':
    N = int(input().strip())
    es_par()