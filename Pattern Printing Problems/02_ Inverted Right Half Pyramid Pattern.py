# Inverted Right Half Pyramid Pattern

# Given an integer N, print N rows of an inverted right half pyramid pattern. In an inverted right half pattern of N rows, the first row has N number of stars, the second row has (N - 1) number of stars, and so on till the Nth row, which has only 1 star.

# Examples:

# Input: n = 5
# Output:
# *****
# ****
# ***
# **
# *

# Input: n = 3
# Output:
# ***
# **
# *

class Solution:
    def inverted_half_pyramid(self, n):
        
        for i in range(1, n + 1):
            
            for j in range(1, n - i + 2):
                
                print("*", end="")
            
            print()
            
# Approach -  we are using two nested loops. The outer loop runs from 1 to n (inclusive) to handle the number of rows. The inner loop runs from 1 to (n - i + 1) to print the stars in each row. After printing the stars for each row, we print a newline character to move to the next row.