# half Diamond star pattern
# Given an integer N, the task is to print half-diamond-star pattern.


# Examples:

# Input: N = 3
# Output:
# *
# **
# ***
# **
# *

# Input: N = 6
# Output:
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *


class Solution:
    def halfDiamondStar(self, N):
        # Increasing part
        for i in range(1, N + 1):
            print("*" * i)

        # Decreasing part
        for i in range(N - 1, 0, -1):
            print("*" * i)
            
# Approach
# Print stars from 1 to N (increasing pattern).
# Then print stars from N-1 to 1 (decreasing pattern).
# Use "*" * i to print i stars in each row.

# This forms a half-diamond pattern.