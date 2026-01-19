# Sort 0s, 1s and 2s 

# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Note: You need to solve this problem without utilizing the built-in sort function.

# Examples
"""
Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.

"""

# Solution:

class Solution:
    def sort012_counting(self, arr):
        count0 = 0
        count1 = 0
        count2 = 0

        for num in arr:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        index = 0

        for _ in range(count0):
            arr[index] = 0
            index += 1

        for _ in range(count1):
            arr[index] = 1
            index += 1

        for _ in range(count2):
            arr[index] = 2
            index += 1

        return arr 
      