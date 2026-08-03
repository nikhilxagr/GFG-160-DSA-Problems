# Count Digits in a Number

# Given a number n, return the count of digits in this number.

# Examples :

# Input: n = 1567
# Output: 4
# Explanation: There are 4 digits in 1567, which are 1, 5, 6 and 7.
# Input: n = 99999
# Output: 5
# Explanation: Number of digit in 99999 is 5

class Solution:
    def countDigits(self, n):
        num = str(n)

        # If negative, exclude '-' sign
        
        if num[0] == '-':
            return len(num) - 1

        return len(num)