# Problem Statement:

# Maximum Circular Subarray Sum

# You are given a circular array arr[] of integers, find the maximum possible sum of a non-empty subarray. In a circular array, the subarray can start at the end and wrap around to the beginning. Return the maximum non-empty subarray sum, considering both non-wrapping and wrapping cases.
# Note: A subarray may wrap around the end and continue from the beginning, forming a circular segment.

# Examples: 
"""

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.

Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].

Input: arr[] = [5, -2, 3, 4]
Output: 12
Explanation: The circular subarray [3, 4, 5] gives the maximum sum of 12.
"""

# Algorithm Steps

# Find max subarray sum (Kadane)
# Find min subarray sum (Reverse Kadane)
# Find total sum
# Answer = max(normal max, circular max)

# Solution:

class Solution:
    def maxCircularSum(self, arr):
        total = arr[0]
        
        cur_max =  max_sum = arr[0]
        cur_min = min_sum = arr[0]
        
        for i in range(1, len(arr)):
            num = arr[i]
            total += num

            # Kadane for max subarray
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)

            # Kadane for min subarray
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)

        # All elements are negative
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)
    
if __name__ == "__main__":
    solve = Solution()
    arr = [8, -8, 9, -9, 10, -11, 12]
    print(solve.maxCircularSum(arr))