# Divisible by 13

# Given a number represented as a string s (which may be very large), check whether it is divisible by 13 or not.

# Examples:

# Input : s = "2911285"
# Output : true
# Explanation: 2911285 / 13 = 223945, which is a whole number with no remainder.
# Input : s = "27"
# Output : false
# Explanation: 27 / 13 ≈ 2.0769..., which is not a whole number (there is a remainder).

 
class Solution:
    def divby13(self, s):
        rem = 0

        for ch in s:
            rem = (rem * 10 + int(ch)) % 13

        return rem == 0
    
# Approach - we use the property of modulus to check divisibility by 13. We iterate through each character in the string, updating the remainder when divided by 13. If the final remainder is 0, then the number is divisible by 13.