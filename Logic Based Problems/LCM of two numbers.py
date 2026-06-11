# LCM of two numbers

# You are given two positive integers a and b Your task is to compute and return the Least Common Multiple (LCM) of the two numbers.
# The LCM of two integers is the smallest positive integer that is divisible by both a and b.

# Examples:

# Input: a = 12, b = 18
# Output: 36
# Explanation: LCM of 12 and 18 is 36
# Input: a = 5, b = 11
# Output: 55
# Explanation: LCM of 5 and 11 is 55

class Solution:
    def lcm(self, a, b):

        g = max(a, b) 
    
        s = min(a, b)  

        for i in range(g, a * b + 1, g):
            
            if i % s == 0:
                return i
                
        return a * b 
  
# Using GCD LCM Formula
   
# # function for gcd

# def gcd(a, b):
#     return a if b == 0 else gcd(b, a % b)

# def lcm(a, b):
#     return (a // gcd(a, b)) * b

# if __name__ == '__main__':
#     a = 10
#     b = 5
#     print(lcm(a, b))