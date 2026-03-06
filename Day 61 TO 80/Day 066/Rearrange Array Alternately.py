# Rearrange Array Alternately

# Given an array of positive integers. Your task is to rearrange the array elements alternatively i.e. first element should be the max value, the second should be the min value, the third should be the second max, the fourth should be the second min, and so on.
# Note: Modify the original array itself. Do it without using any extra space. You do not have to return anything.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5, 6]
# Output: [6, 1, 5, 2, 4, 3]
# Explanation: Max element = 6, min = 1, second max = 5, second min = 2, and so on... The modified array is: [6, 1, 5, 2, 4, 3]

# Input: arr[]= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# Output: [110, 10, 100, 20, 90, 30, 80, 40, 70, 50, 60]
# Explanation: Max element = 110, min = 10, second max = 100, second min = 20, and so on... Modified array is : [110, 10, 100, 20, 90, 30, 80, 40, 70, 50, 60]

# Input: arr[]= [1]
# Output: [1]

class Solution:
    def rearrange(self, arr):
        arr.sort()
        left = 0
        right = len(arr) - 1
        ans = []

        while left <= right:
            ans.append(arr[right])   # add max
            right -= 1
            
            if left <= right:
                ans.append(arr[left])  # add min
                left += 1

        for i in range(len(arr)):
            arr[i] = ans[i]
        return arr