# Sum of Squares of First n Natural Numbers

# Given an integer n. The task is to calculate the sum of the squares of the first  n natural numbers.

# Examples:

# Input: n = 2
# Output: 5
# Explanation: 12 + 22 = 5
# Input: n = 3
# Output: 14
# Explanation: 12 + 22 + 32 = 14


class Solution:
    def sumOfSquares(self, number):
       
        sum = 0
        for i in range(1, number + 1):
            sum += i * i
        return sum