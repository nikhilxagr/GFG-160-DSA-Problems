# Nth Fibonacci Number

# Find the n-th Fibonacci number for a given non-negative integer n.
# The Fibonacci sequence is defined as:

# F(0) = 0
# F(1) = 1
# F(n) = F(n - 1) + F(n - 2) for n ≥ 2
# Examples :

# Input: n = 5
# Output: 5
# Explanation: The 5th Fibonacci number is 5.
# Input: n = 0
# Output: 0 
# Explanation: The 0th Fibonacci number is 0.
# Input: n = 1
# Output: 1
# Explanation: The 1st Fibonacci number is 1.

class Solution:
    def nthFibonacci(self, n: int) -> int:
        
        if n <= 1:
            return n

        # stores current Fibonacci number
        curr = 0

        # To store the previous  two Fibonacci numbers
        
        prev1 = 1
        prev2 = 0

        for i in range(2, n + 1):
            
            curr = prev1 + prev2

        # Update previous two Fibonacci numbers for next number
        
            prev2 = prev1
            prev1 = curr

        return curr