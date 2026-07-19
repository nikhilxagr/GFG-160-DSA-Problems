# Stair Case Patterns
# Programs to print following pattern.
# Examples: 

# Input : 6
# Output :
# * *
# * *
# * * * *
# * * * *
# * * * * * *
# * * * * * *

class Solution:
    def stair_case_pattern(self, n):
        for i in range(1, n + 1):
            stars = ((i + 1) // 2) * 2
            print("* " * stars)        