# All divisors of a Number
# Given an integer n, return all the divisors of n in the ascending order.
 
# Examples:

# Input : n = 20
# Output: 1 2 4 5 10 20
# Explanation: 20 is completely divisible by 1, 2, 4, 5, 10 and 20.
# Input: n = 21191
# Output: 1 21191
# Explanation: As 21191 is a prime number, it has only 2 factors(1 and the number itself).


class Solution:
    def getDivisors(self, n):
        
        divisors = []
        
        for i in range(1, int(n**0.5) + 1):
            
            if n % i == 0:
                divisors.append(i)
                
                if i != n // i:  # Avoid adding the square root twice for perfect squares
                    
                    divisors.append(n // i)
        
        return sorted(divisors)  # Return the divisors in ascending order
    
# Approach -
# we iterate from 1 to the square root of n. 
# For each integer i, if n is divisible by i, we add both i and n // i to the list of divisors. Finally,
# we sort the list of divisors before returning it.
# This method ensures that we efficiently find all divisors without unnecessary iterations. 