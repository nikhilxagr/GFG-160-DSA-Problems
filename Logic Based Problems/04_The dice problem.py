# The dice problem
 
# You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. Given the face of this cube, find the number on the opposite side of the cube.

# Examples:

# Input: n = 6
# Output: 1
# Explanation: For dice facing number 6 opposite face will have the number 1.
# Input: n = 2
# Output: 5
# Explanation: For dice facing number 5 opposite face will have the number 2.

class Solution:
    def oppositeFaceOfDice(self, n):
        # The opposite faces of a standard dice add up to 7
        return 7 - n