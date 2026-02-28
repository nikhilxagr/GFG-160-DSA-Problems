# Sort 0s, 1s and 2s

# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Note: You need to solve this problem without utilizing the built-in sort function.

# Examples:

# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.

# Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.


class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
                
            elif arr[mid] == 1:
                mid += 1
                
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
                
# sol = Solution()
# arr = [0, 1, 2, 0, 1, 2]
# print("Before sorting:", arr)
# sol.sort012(arr)
# print("After sorting:", arr)