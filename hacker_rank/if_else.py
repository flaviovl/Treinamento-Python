# Given an integer, n, perform the following conditional actions:

# If  n is odd, print Weird
# If  n is even and in the inclusive range of 2 to 5, print Not Weird
# If  n is even and in the inclusive range of 6 to 20, print Weird
# If  n is even and greater than 20, print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

import math
import os
import random
import re
import sys


def structural_matching(n: int) -> str:
    match n:
        case 2 | 4: 
            return "Not Weird"
        
        case _: 
            if n % 2 != 0 and n > 20:
                return "Weird"
            else:
                return "Not Weird"

# -------------------------------------------------------------------------------------------------
def solution1(n):
    if n % 2 != 0 or n not in range(2, 6) and n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
# -------------------------------------------------------------------------------------------------
def solution2(n):
    if n % 2 != 0:
        print("Weird")
    elif n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
# -------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    n = int(input("Digite um Inteiro: ").strip())

    solution1(n)
    solution2(n)
    print(structural_matching(n))
