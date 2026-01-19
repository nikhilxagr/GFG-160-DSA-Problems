# Problem Statement:
# String to Integer - Write your own atoi()

# Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

# Cases for atoi() conversion:

# Skip any leading whitespaces.
# Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
# Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
# If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.

# Examples:

"""
Examples:

Input: s = "-123"
Output: -123
Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer

Input: s = "  -"
Output: 0
Explanation: No digits are present, therefore the returned answer is 0.

Input: s = " 1231231231311133"
Output: 2147483647
Explanation: The converted number will be greater than 231 – 1, therefore print 231 – 1 = 2147483647.

Input: s = "-999999999999"
Output: -2147483648
Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.

Input: s = "  -0012gfg4"
Output: -12
Explanation: After ignoring leading zeros nothing is read after -12 as a non-digit character ‘g’ was encountered.
"""

# Solution:

class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        num = 0

        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Read digits
        while i < n and '0' <= s[i] <= '9':
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        num *= sign

        # 4. Clamp to 32-bit integer range
        if num > 2**31 - 1:
            return 2**31 - 1
        if num < -2**31:
            return -2**31

        return num
    
if __name__ == "__main__":
    solve = Solution()
    
    s1 = "-123"
    print(solve.myAtoi(s1))
    
    s2 = "  -"
    print(solve.myAtoi(s2))
    
    
# Approach:

# 1. We start by skipping any leading whitespaces in the string.
# 2. Next, we check for a sign ('+' or '-') and set the sign variable accordingly.
# 3. We then read the digits from the string, constructing the integer value while ignoring
#    any leading zeros.
# 4. Finally, we clamp the integer value to the 32-bit signed integer range and return the result.  
    