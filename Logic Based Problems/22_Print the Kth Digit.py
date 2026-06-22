# Print the Kth Digit


# Given two numbers a and b, find kth digit from right of ab.

# Example 1:

# Input: a = 3, b = 3, k = 1
# Output: 7
# Explanation: 33 = 27 and 1st digit from right is 7
# Input: a = 5, b = 2, k = 2
# Output: 2
# Explanation: 52 = 25 and second digit from right is 2.
# Constraints:
# 1 <= a,b <= 15
# 1 <= k <= digits in ab

class Solution:
    def kthDigit(self, a, b, k):
       
        mod = 10 ** k
        res = 1
        base = a

        while b > 0:
            
            if b & 1:
                res = (res * base) % mod
                
            base = (base * base) % mod
            
            b = b >>  1

        for i in range(1, k):
            res //= 10
            
        return res

# Approach

# Computes the value of a to the power of b
# Then iterates through the digits of the result. Starting from the rightmost digit, it extracts each digit one by one by using the modulus operation (p % 10).
# The extracted digit is compared with the desired position k. It continues removing the last digit (using integer division by 10) until it reaches the k-th digit, which is then returned.