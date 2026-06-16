# Next sparse binary number

# Given an integer n in the input, find its next sparse binary number.A sparse binary number is a number whose binary representation does not contain any consecutive 1s.

# Example 1:

# Input: n = 3
# Output: 4
# Explanation: Binary representation of 4
# is 0100.
# Example 2:

# Input: n = 5
# Output: 5
# Explanation: Binary representation of 5
# is 0101.

class Solution:
    def nextSparse (ob, n):
        
        while True:
            if (n & (n >> 1)) == 0:
                return n
            n += 1
