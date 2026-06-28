# Modular Exponentiation

# Given three integers x, n, and M, compute (x^n) % M, i.e., the remainder when x raised to the power n is divided by M.

# Examples:

# Input: x = 3, n = 2, M = 4
# Output: 1
# Explanation: 32 % 4 = 9 % 4 = 1.
# Input: x = 2, n = 6, M = 10
# Output: 4
# Explanation: 26 % 10 = 64 % 10 = 4.

class Solution:
    def powMod(self, x, n, M):

        # Base case
        if n == 0:
            return 1 % M

        # Recursive call
        temp = self.powMod(x, n // 2, M)
        temp = (temp * temp) % M

        # If n is even
        if n % 2 == 0:
            return temp
        else:
            return (x * temp) % M
        
# Approach - in this solution, we use the method of exponentiation by squaring to compute (x^n) % M efficiently. The algorithm works as follows:
# 1. If n is 0, return 1 % M (base case).
# 2. Recursively compute (x^(n//2)) % M and store it in a temporary variable.
# 3. Square the temporary variable and take modulo M.
# 4. If n is even, return the squared value; if n is odd, multiply by x and take modulo M before returning the result.
        