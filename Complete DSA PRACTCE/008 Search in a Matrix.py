# Search in a Matrix

# Given a 2D integer array mat[][] and a number x, find whether element x is present in the matrix or not.

# Examples:

# Input: mat[][] = [[6, 23, 21],[4, 45, 32],[69, 11, 87]], x = 32
# Output: true
# Explanation: 32 is present in the matrix, so the output is 1.
# Input: mat[][] = [[14, 34, 23, 95, 43, 28]], x = 55
# Output: false
# Explanation: 55 is not present in the matrix, so the output is 0.
# Input: mat[][] = [[87, 9, 99],[101, 3, 111]], x = 101
# Output: true
# Explanation: 101 is present in the matrix.

class Solution:
    def searchMatrix(self,matrix, x):
        
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])):
                
                if matrix[i][j] == x:
                    return True
        return False
    
obj = Solution()
matrix = [[6, 23, 21],[4, 45, 32],[69, 11, 87]]
x = 32
print(obj.searchMatrix(matrix, x))