# calculate the value of nPr
# Write a program to calculate nPr . nPr  represents n permutation r and value of nPr  is (n!) / (n-r)!.

# Examples:

# Input: n = 5, r = 2
# Output: 20
# Explaination: 5!/(5-2)! = 5!/3! = 120/6 = 20.
# Input: n = 6, r = 3
# Output: 120
# Explaination: 6!/(6-3)! = 6!/3! = 720/6 = 120.

class Solution:
    def nPr(self, n, r):
        
        # calculate factorial
        
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            else:
                return num * factorial(num - 1)

        # Calculate nPr using the formula nPr = n! / (n - r)!
        
        if r > n:
            return 0    # If r is greater than n, nPr is not defined
        
        else:
            return factorial(n) // factorial(n - r)
        
# Approach - 
# We can calculate nPr using the formula nPr = n! / (n - r)!.
# We can define a helper function to calculate the factorial of a number.
# Then, we can use this helper function to calculate n! and (n - r)! and
# return the result of nPr. If r is greater than n, we can return 0 since nPr is not defined in that case.