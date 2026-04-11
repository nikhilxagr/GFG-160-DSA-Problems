# Maximum product of two numbers


# Given an array arr of non-negative integers, return the maximum product of two numbers possible.

# Example:

# Input: arr[] = [1, 4, 3, 6, 7, 0] 
# Output: 42
# Explanation: 6 and 7 have the maximum product.
# Input: arr[] = [1, 100, 42, 4, 23]
# Output: 4200
# Explanation:  42 and 100 have the maximum product.


class Solution:
    def maxProduct(self,arr):
        if len(arr) < 2:
            return 0

        largest = -1
        next_large = -1

        for num in arr:
            
            if num > largest:
                next_large = largest
                largest = num
                
            elif num > next_large:
                next_large = num

        return largest * next_large
    
# Algorithm
# 1. Initialize two variables largest and next_large to -1.
# 2. Iterate through each number in the array: 
#    a. If the current number is greater than largest, update next_large to largest and largest to the current number.
#    b. Else if the current number is greater than next_large, update next_large to the current number.
# 3. After the loop, return the product of largest and next_large as the maximum product of two numbers in the array.