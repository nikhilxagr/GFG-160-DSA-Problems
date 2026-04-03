# Given a string S, Check if characters of the given string can be rearranged to form a palindrome.
# Note: You have to return 1 if it is possible to convert the given string into palindrome else return 0. 

# Example 1:

# Input:
# S = "geeksogeeks"
# Output: Yes
# Explanation: The string can be converted
# into a palindrome: geeksoskeeg

# Example 2:

# Input: 
# S = "geeksforgeeks"
# Output: No
# Explanation: The given string can't be
# converted into a palindrome.

#User function Template for python3

class Solution:

    def isPossible(self, S):
     
        count = {}
        
        for i in S:
            
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        odd_count = 0
        
        for key in count:
            
            if count[key] % 2 != 0:
                odd_count += 1
        if odd_count > 1:
            return 0
        
        return 1