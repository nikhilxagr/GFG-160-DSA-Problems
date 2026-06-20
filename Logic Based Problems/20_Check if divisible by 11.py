# Given a number s . Check whether it is divisble by 11 or not.

# Examples:

# Input: s = 76945
# Output: true
# Explanation: The number is divisible by 11 as 76945 % 11 = 0.
# Input: s = 12
# Output: false
# Explanation: The number is not divisible by 11 as 12 % 11 = 1.

class Solution:
    def divisibleBy11(self, s: str) -> bool:
        
        # Convert the string to an integer
        num = int(s)
        
        # Check if the number is divisible by 11
        return num % 11 == 0