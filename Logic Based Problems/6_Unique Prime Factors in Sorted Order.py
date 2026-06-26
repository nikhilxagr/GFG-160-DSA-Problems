# Unique Prime Factors in Sorted Order

# Given a number n. Find its unique prime factors in increasing order.

# Examples :

# Input: n = 100
# Output: [2, 5]
# Explanation: Unique prime factors of 100 are 2 and 5.
# Input: n = 60
# Output: [2, 3, 5]
# Explanation: Prime factors of 60 are 2, 2, 3, 5. Unique prime factors are 2, 3 and 5.

class Solution:
    def primeFac(self, n):
        
        unique_factors = []

        if n % 2 == 0:
            unique_factors.append(2)
            while n % 2 == 0:
                n //= 2
    
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                unique_factors.append(i)
                while n % i == 0:
                    n //= i
        
        if n > 2:
            unique_factors.append(n)
        
        return unique_factors
        
Approach - in this approach , we use factors that is used 