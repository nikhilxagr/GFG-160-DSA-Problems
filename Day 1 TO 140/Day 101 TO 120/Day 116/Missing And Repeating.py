# Missing And Repeating

# Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.

# Examples:

# Input: arr[] = [2, 2]
# Output: [2, 1]
# Explanation: Repeating number is 2 and the missing number is 1.
# Input: arr[] = [1, 3, 3] 
# Output: [3, 2]
# Explanation: Repeating number is 3 and the missing number is 2.
# Input: arr[] = [4, 3, 6, 2, 1, 1]
# Output: [1, 5]
# Explanation: Repeating number is 1 and the missing number is 5.


class Solution:
    def findTwoElement(self, arr):
        
        n = len(arr)
        total_sum = n * (n + 1) // 2
        total_sq_sum = n * (n + 1) * (2 * n + 1) // 6
        
        arr_sum = sum(arr)
        arr_sq_sum = sum(x * x for x in arr)
        diff = arr_sum - total_sum
        
        sq_diff = arr_sq_sum - total_sq_sum
        sum_xy = sq_diff // diff
        
        repeating = (diff + sum_xy) // 2
        
        missing = repeating - diff
        
        return [repeating, missing]