# Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

# Examples:

# Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
# Output: 3
# Explanation: Minimum length subarray is [4, 45, 6]
# Input: x = 100, arr[] = [1, 10, 5, 2, 7]
# Output: 0
# Explanation: No subarray exist

class Solution:
    def smallestSubWithSum(self, x, arr):
        
        n = len(arr)
        
        min_length = float('inf')
        
        current_sum = 0
        start = 0

        for end in range(n):
            
            current_sum += arr[end]

            while current_sum > x:
                
                min_length = min(min_length, end - start + 1)
                current_sum -= arr[start]
                start += 1

        return min_length if min_length != float('inf') else 0