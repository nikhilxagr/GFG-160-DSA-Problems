# Min Chars to Add for Palindrome

# Palindrome by Front Insertion

# Given a string s consisting of only lowercase English letters, find the minimum number of characters that need to be added to the front of s to make it a palindrome.
# Note: A palindrome is a string that reads the same forward and backward.

# Examples :
    
"""
Input: s = "abc"
Output: 2
Explanation: We can make above string palindrome as "cbabc", by adding 'b' and 'c' at front.

Input: s = "aacecaaaa"
Output: 2
Explanation: We can make above string palindrome as "aaaacecaaaa" by adding two a's at front of string.
    
"""
    
# Solution:

class Solution:
    def minChar(self, s):
        n = len(s)
        rev = s[::-1]
        temp = s + "$" + rev

        lps = [0] * len(temp)
        j = 0

        for i in range(1, len(temp)):
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]

            if temp[i] == temp[j]:
                j += 1
                lps[i] = j

        return n - lps[-1]


solution = Solution()
print(solution.minChar("abc")) 
print(solution.minChar("aacecaaaa"))
