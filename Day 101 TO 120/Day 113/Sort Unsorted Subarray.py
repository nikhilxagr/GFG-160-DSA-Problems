# Sort Unsorted Subarray

# Given an unsorted array arr[]. Find the subarray arr[s...e] such that sorting this subarray makes the whole array sorted.

# Note: If the given array is already sorted then return [0, 0].

# Examples:

# Input: arr[] = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
# Output: [3, 8]
# Explanation: Sorting subarray starting from index 3 and ending at index 8 results in sorted array. Initial array: [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], Final array: [10, 12, 20, 25, 30, 31, 32, 35, 40, 50, 60](After sorting the bold part).
# Input: arr[] = [0, 1, 15, 25, 6, 7, 30, 40, 50]
# Output: [2, 5]
# Explanation: Sorting subarray starting from index 2 and ending at index 5 results in sorted array. Initial array: [0, 1, 15, 25, 6, 7, 30, 40, 50], Final array: [0, 1, 6, 7, 15, 25, 30, 40, 50](After sorting the bold part).
class Solution:
    def printUnsorted(self, arr):
        sorted_arr = sorted(arr)
        
        start = -1
        end = -1
        
        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                if start == -1:
                    start = i
                end = i
        
        if start == -1:
            return [0, 0]
        
        return [start, end]