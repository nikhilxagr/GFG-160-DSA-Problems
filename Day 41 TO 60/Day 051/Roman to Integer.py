# Roman to Integer

# Given a string s in Roman number format, your task is to convert it to an integer. Various symbols and their values are given below.
# Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

# Examples:

# Input: s = "IX"
# Output: 9
# Explanation: IX is a Roman symbol which represents 10 – 1 = 9.
# Input: s = "XL"
# Output: 40
# Explanation: XL is a Roman symbol which represents 50 – 10 = 40.
# Input: s = "MCMIV"
# Output: 1904
# Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904.


class Solution:
    def romanToDecimal(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                ans = ans - roman[s[i]]
            else:
                ans = ans + roman[s[i]]
                
        return ans
    
    
    
# If next character exists and is bigger → subtract current value from answer
# Else → add current value to answer