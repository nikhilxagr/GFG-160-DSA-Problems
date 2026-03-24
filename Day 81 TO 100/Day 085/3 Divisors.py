# 3 Divisors

# You are given a list of q queries, and for each query, an integer n is provided. The task is to find how many numbers less than or equal to n have exactly 3 divisors.

# Examples:

# Input: q = 1
#           query[0] = 6
# Output: 1
# Explanation: There is only one number 4 which has exactly three divisors 1, 2 and 4 and less than equal to 6.
# Input: q = 2
#        query[0] = 6
#        query[1] = 10
# Output: 1
#         2
# Explanation: For query 1 it is covered in the example 1. query 2:There are two numbers 4 and 9 having exactly 3 divisors and less than 
# equal to 10.

class Solution:
    def isPrime(self, x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def threeDivisors(self, query, q):
        ans = []
        
        for n in query:
            count = 0
            limit = int(n ** 0.5)
            
            for i in range(2, limit + 1):
                if self.isPrime(i):
                    count += 1
            
            ans.append(count)
        
        return ans