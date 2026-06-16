# Three Great Candidates

# The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 3 candidates are great collectively if the product of their abilities is maximum. Given the abilities of some candidates in an array, arr[], return the maximum collective ability from the pool of candidates.

# Examples:

# Input: arr[] = [10, 3, 5, 6, 20]
# Output: 1200
# Explanation: Multiplication of 10, 6, and 20 is 1200.
# Input: arr[] = [-10, -3, -5, -6, -20]
# Output: -90
# Explanation: Multiplication of -3, -5 and -6 is -90.

class Solution:
    def maxProduct(self, arr):
        arr.sort()
        return max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])
    
    
# arr = [10, 3, 5, 6, 20]
# arr.sort()
# print(arr[-1] * arr[-2] * arr[-3])