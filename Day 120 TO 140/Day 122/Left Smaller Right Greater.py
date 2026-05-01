# Left Smaller Right Greater

# Given an unsorted array arr[], find the first element such that every element to its left is less than or equal to it, and every element to its right is greater than or equal to it.

# Note: If no such element exists, return -1.

# Examples : 

# Input: arr = [4, 2, 5, 7]
# Output: 5
# Explanation: All elements to the left of 5 are less than or equal to 5, and all elements to the right are greater than or equal to 5.
# Input: arr = [11, 9, 12]
# Output: -1
# Explanation: No element in the array satisfies the required condition.

class Solution:
    def findElement(self, arr):
        
        n = len(arr)
        if n == 0:
            return -1

        left_max = [0] * n
        right_min = [0] * n

        left_max[0] = arr[0]
        
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])

        right_min[n - 1] = arr[n - 1]
        
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], arr[i])

        for i in range(1, n - 1):
            if left_max[i - 1] <= arr[i] and right_min[i + 1] >= arr[i]:
                return arr[i]

        return -1