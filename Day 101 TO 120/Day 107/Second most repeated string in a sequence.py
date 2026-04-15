# Second most repeated string in a sequence

# Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.

# Note: No two strings are the second most repeated, there will be always a single string.

# Example 1:

# Input:
# N = 6
# arr[] = {aaa, bbb, ccc, bbb, aaa, aaa}
# Output: bbb
# Explanation: "bbb" is the second most 
# occurring string with frequency 2.

# Example 2:

# Input: 
# N = 6
# arr[] = {geek, for, geek, for, geek, aaa}
# Output: for
# Explanation: "for" is the second most
# occurring string with frequency 2.

#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        
        strCount = {}

        for string in arr:
            strCount[string] = strCount.get(string, 0) + 1

        sorted_strings = sorted(strCount.items(), key=lambda x: x[1], reverse=True)

        return sorted_strings[1][0]
