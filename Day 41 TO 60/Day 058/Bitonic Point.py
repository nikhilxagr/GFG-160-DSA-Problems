# Bitonic Point

# Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
# Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.

# Note: It is guaranteed that the array contains exactly one bitonic point.

# Examples:

# Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
# Output: 8
# Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].
# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 50
# Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.
# Input: arr[] = [120, 100, 80, 20, 0]
# Output: 120
# Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].


class Solution:
    def findMaximum(self, arr):
        n = len(arr)
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return arr[i]
        return arr[0] if arr[0] > arr[-1] else arr[-1]

# Driver Code
arr1 = [1, 2, 4, 5, 7, 8, 3]
arr2 = [10, 20, 30, 40, 50]
arr3 = [120, 100, 80, 20, 0]

sol = Solution()
print(sol.findMaximum(arr1))  # Output: 8
print(sol.findMaximum(arr2))  # Output: 50
print(sol.findMaximum(arr3))  # Output: 120