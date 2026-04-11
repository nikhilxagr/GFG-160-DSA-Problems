# You are given an integer n. You need to convert all zeroes of n to 5.

# Examples:

# Input: n = 1004
# Output: 1554
# Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
# Input: n = 121
# Output: 121
# Explanation: Since there are no zeroes in 121, the number remains as 121.


class Solution:
    def convertFive(self, n):
        
        n_str = str(n)
        
        n_str = n_str.replace('0', '5')
        
        return int(n_str)