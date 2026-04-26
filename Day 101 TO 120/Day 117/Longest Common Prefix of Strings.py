# Longest Common Prefix of Strings

# Given an array of strings arr[]. Return the longest common prefix among each and every strings present in the array. If there's no prefix common in all the strings, return "".

# Examples :

# Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
# Output: "gee"
# Explanation: "gee" is the longest common prefix in all the given strings.
# Input: arr[] = ["hello", "world"]
# Output: ""
# Explanation: There's no common prefix in the given strings.

#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        
        if not arr:
            return ""

        prefix = arr[0]

        for i in range(1, len(arr)):
            
            while not arr[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix