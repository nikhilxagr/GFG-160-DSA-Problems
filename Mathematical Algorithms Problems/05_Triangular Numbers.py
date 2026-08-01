# Triangular Numbers

# Given a number n, check whether it is a triangular number or not. Return 1 if it is a triangular number, otherwise return 0.

# Note: A number is a triangular number if it can be represented in the form of a triangular grid of points, where each row contains as many points as its row number. The first few triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4), and so on.

# Examples:

# Input: n = 55
# Output: 1
# Explanation: 55 is a triangular number. It can be represented in 10 rows.
# Input: n = 56
# Output: 0
# Explanation: 56 is not a triangular number. 

class Solution:
    def isTriangular(self, num):
        if num < 0:
            return 0
        
    
        dicr = 1 + 8 * num
        
       
        Sqr_dicr = int(dicr**0.5)
        
        if Sqr_dicr * Sqr_dicr == dicr:
            return 1
        else:
            return 0
        
        
# A triangular number can be represented as n(n+1)/2 for some integer n.
# We can rearrange this to form a quadratic equation: n^2 + n - 2*num = 0
# The discriminant of this equation must be a perfect square for n to be an integer.
# Calculate the discriminant
# Check if the discriminant is a perfect square