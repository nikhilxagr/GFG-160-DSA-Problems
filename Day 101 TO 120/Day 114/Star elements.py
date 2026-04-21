# Star elements

# Given an unsorted array arr. Find all the star elements in the array. Star elements are those elements that are strictly greater than all the elements on its right side.

# Note: Assume the first element is greater than all the elements on its left side and the last element is greater than all the elements on its right side.

# Examples:

# Input: arr[] = [1, 6, 5, 4, 7, 8, 4, 3, 2, 1]
# Output: [8, 4, 3, 2, 1] 
# Explanation: Star elements are 8, 4, 3, 2 and 1.

# Input: arr[] = [1, 2, 10, 3, 4, 5, 8, 10, 4]
# Output: [10, 4] 
# Explanation: Star elements are 10 and 4.



class Solution:
    def getStar(self, arr):
        max_so_far = float('-inf')
        result = []

        # Traverse from right
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > max_so_far:
                result.append(arr[i])
                max_so_far = arr[i]

        return result[::-1]
