# Left Half Pyramid Pattern

# Given an integer N, the task is to print N rows of left half pyramid pattern. In left half pattern of N rows, the first row has 1 star, second row has 2 stars and so on till the Nth row which has N stars. All the stars are right aligned.

# Examples:

# Input: 3
# Output: 
#     *
#   **
# ***

# Input: 5
# Output: 
#         *
#       **
#     ***
#   ****
# *****

# Approach:

# The problem can be solved using two nested loops inside another loop. The outer loop will run for the rows and the first inner loop will print the spaces and second loop will print stars. If we observe carefully, if we have a left half pyramid pattern with N rows, the 1st row will have 4 spaces followed by 1 star, the 2nd row will have 3 spaces followed by 2 stars, the third row will have 2 spaces followed by 3 stars and so on. So, Nth row will have 0 spaces followed by N stars.

class Solution:
    def left_half_pyramid(self, n):
        
        for i in range(1, n + 1):
            
            for j in range(1, n - i + 1):
                
                print(" ", end="")
            
            for k in range(1, i + 1):
                
                print("*", end="")
            
            print()