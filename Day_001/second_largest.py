# Second Largest Element in an Array

# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

# Note: If the second largest element does not exist, return -1.

# Solution comming soon!........

# I am Back with the solution

# Examples

"""
Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second 

largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second

largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
"""

class Solution:
    def getSecondLargest(self, arr):
        first = -1
        second = -1

        for num in arr: 
            if num > first:
                second = first
                first = num
            else:
                if num > second and num < first:
                    second = num

        return second
