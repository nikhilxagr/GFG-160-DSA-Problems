# Given two positive integers a and b, find GCD of a and b.

# Note: Don't use the inbuilt gcd function

# Examples:

# Input: a = 20, b = 28
# Output: 4
# Explanation: GCD of 20 and 28 is 4
# Input: a = 60, b = 36
# Output: 12
# Explanation: GCD of 60 and 36 is 12

class Solution:
    def gcd(self, a, b):
        
        if b == 0:
            return a
        
        return self.gcd(b, a % b)