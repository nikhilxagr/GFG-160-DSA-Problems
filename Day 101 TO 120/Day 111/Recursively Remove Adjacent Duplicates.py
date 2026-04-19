# Recursively Remove Adjacent Duplicates

# Given a string s, remove all its adjacent duplicate characters recursively, until there are no adjacent duplicate characters left.

# Note: If the resultant string becomes empty, return an empty string.

# Examples:

# Input: s = "geeksforgeek"
# Output: "gksforgk"
# Explanation:  g(ee)ksforg(ee)k -> gksforgk
# Input: s = "abccbccba"
# Output: ""
# Explanation: ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->""(empty string)
# Input: s = "abcd"
# Output: "abcd"
# Explanation: There are no adjacent duplicate characters


class Solution:
    def removeUtil(self, S):
        if len(S) <= 1:
            return S

        # Build groups for one pass, then remove groups with length > 1.
        stack = []

        for ch in S:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])

        reduced = "".join(ch for ch, count in stack if count == 1)

        # If this pass changed the string, process again recursively.
        if reduced != S:
            return self.removeUtil(reduced)

        return reduced