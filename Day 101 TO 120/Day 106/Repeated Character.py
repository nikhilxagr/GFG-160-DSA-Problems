# Repeated Character

# Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

# NOTE - If there are no repeating characters return '#'.

# Example 1:

# Input:
# S = "geeksforgeeks"
# Output: g
# Explanation: g, e, k and s are the repeating
# characters. Out of these, g occurs first. 
# Example 2:

# Input: 
# S = "abcde"
# Output: -1
# Explanation: No repeating character present. (You need to return '#')

#User function Template for python3

class Solution:
    def firstRep(self, s):
        # code here
        char_count = {}
        
        for char in s:
            if char in char_count:
                return char
            else:
                char_count[char] = 1
        
        return '#'