# N-th Term of GP

# Given three integers a, r, and n, where a is the first term of a geometric progression (GP), r is the common ratio, and n is the position of the term you need to find. Your task is to calculate the n-th term of the GP.
# Since the result can be very large, return the answer modulo 1000000007 (i.e. 109+ 7).

# Examples:

# Input: a = 2, r = 2, n = 4
# Output: 16
# Explanation: The GP series is 2, 4, 8, 16, 32,... in which 16 is the 4th term.
# Input: a = 4, r = 3, n = 3
# Output: 36
# Explanation: The GP series is 4, 12, 36, 108,... in which 36 is the 3rd term.

class Solution:
	def nthTerm(self, a, r, n):
     
    # Calculate the n-th term of the GP using the formula: nth_term = a * (r ** (n - 1))
        
        nth_term = a * pow(r, n - 1, 1000000007) % 1000000007
        
        return nth_term