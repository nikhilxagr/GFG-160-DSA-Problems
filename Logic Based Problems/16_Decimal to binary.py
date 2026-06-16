# Decimal to binary

# Given a decimal integer n, convert it and return its binary equivalent as a string.

# Examples :

# Input: n = 12
# Output: 1100
# Explanation: The binary representation of 12 is "1100", since 12 = 1×23 + 1×22 + 0×21 + 0×20
# Input: n = 33
# Output: 100001
# Explanation: The binary representation of 33 is "100001", since 33 = 1×25 + 0×24 + 0×23 + 0×22 + 0×21 + 1×20

class Solution:
    def decToBinary(self, n):
    
        binary = ""
        
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2
            
        return binary