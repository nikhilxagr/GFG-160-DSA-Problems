# Adding One to Array

# Given a non-negative integer(without leading zeroes) represented as an array arr. Your task is to add 1 to the number (increment the number by 1). The digits are stored such that the most significant digit is at the starting index of the array.

# Examples:

# Input: arr[] = [5, 6, 7, 8]
# Output: [5, 6, 7, 9]
# Explanation: 5678 + 1 = 5679
# Input: arr[] = [9, 9, 9]
# Output: [1, 0, 0, 0]
# Explanation: 999 + 1 = 1000



class Solution:
    def addOne(self, arr):
        
        n = len(arr)
        remainder = 1

        for i in range(n - 1, -1, -1):
            
            total = arr[i] + remainder
            arr[i] = total % 10
            remainder = total // 10

        if remainder:
            arr.insert(0, remainder)

        return arr