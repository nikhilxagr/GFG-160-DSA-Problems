# Nth Catalan Number


# Given a number n, the task is to find the nth catalan number.  Catalan Number for n is equal to the number of expressions containing n pairs of parenthesis that are correctly matched, i.e., for each of the n(' there exist n ')' on there right and vice versa. 

# The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

# Examples:

# Input: n = 3
# Output: 5
# Explanation: Possible expressions are, ((())), (()()), ()(()), (())(), ()()()
# Input: n = 4
# Output: 14
# Explantions: There are total 14 valid combinations which can be formed using 4 parenthesis.


class Solution:
    def findCatalan(self, n):
        
        # Base case
        
        if n <= 1:
            return 1

        # Initialize result
        
        res = 0

        # Calculate value using recursive formula
        
        for i in range(n):
            res += self.findCatalan(i) * self.findCatalan(n - i - 1)

        return res
    
# Approach:
# The nth Catalan number can be calculated using a recursive formula. The formula states that the nth Catalan number can be computed as the sum of the products of pairs of Catalan numbers for all values from 0 to n-1. Specifically, the nth Catalan number C(n) can be expressed as:
# C(n) = C(0) * C(n-1) + C(1) * C(n-2) + ... + C(n-1) * C(0)