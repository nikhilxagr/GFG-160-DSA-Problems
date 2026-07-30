# 03_Nth_Term_of_AP

# Given the first 2 terms a1 and a2 of an Arithmetic Series. Find the nth term of the series. 

# Examples:

# Input: a1 = 2, a2 = 3, n = 4
# Output: 5
# Explanation: The series is: 2,3,4,5,6.... Thus, the 4th term is 5.

# Input: a1 = 1, a2 = 3, n = 10
# Output: 19
# Explanation: The series is: 1,3,5,7,9,11,13,15,17,19,21.. Thus, the 10th term is 19.


class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        
        # Calculate the common difference
        
        d = a2 - a1
        
        # Calculate the nth term using the formula: nth_term = a1 + (n - 1) * d
        
        nth_term = a1 + (n - 1) * d
        
        return nth_term