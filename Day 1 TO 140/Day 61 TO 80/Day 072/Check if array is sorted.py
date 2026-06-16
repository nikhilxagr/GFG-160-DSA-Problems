# Check if array is sorted

# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

# Examples:

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.
# Input: arr[] = [90, 80, 100, 70, 40, 30]
# Output: false
# Explanation: The given array is not sorted.

class Solution:
    def isSorted(self, arr) -> bool:

        for i in range(1, len(arr)):
            
            if arr[i] < arr[i-1]:
                
                return False
            
        return True