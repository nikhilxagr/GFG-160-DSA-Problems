# Power Set

# Given a string s, generate all possible subsequences of the string (including the empty subsequence) and return them in lexicographical order.

# A subsequence is obtained by deleting zero or more characters from the string without changing the relative order of the remaining characters.

# Examples:

# Input : s = "abc"
# Output: ["","a", "ab", "abc", "ac", "b", "bc", "c"]
# Explanation: There are a total of 8 non-empty subsequences for the given string. 
# These subsequences are listed above in lexicographical order.
# Input: s = "aa"
# Output: ["", "a", "a", "aa"]

class Solution:
    def powerSet(self, s):
        ans = []

        def backtrack(index, curr):
            
            # Base Case
            if index == len(s):
                ans.append(curr)
                return

            # Include current character
            
            backtrack(index + 1, curr + s[index])

            # Exclude current character
            
            backtrack(index + 1, curr)

        backtrack(0, "")
        ans.sort()
        
        return ans