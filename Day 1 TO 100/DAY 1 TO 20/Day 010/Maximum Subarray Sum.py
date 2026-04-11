# Maximum Subarray Sum - Kadane's Algorithm

# Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
# Note: A subarray is a continuous part of an array.

# Examples:

"""
Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

"""
class Solution:
    def maxSubarraySum(arr):
        max_sum = arr[0]     
        current_sum = 0   

        for num in arr:
            current_sum = current_sum + num  
            
            if current_sum > max_sum:
                max_sum = current_sum         

            if current_sum < 0:
                current_sum = 0          

        return max_sum
    
    # Algorithm Explanation:
# 1. Start with current_sum = 0
# 2. Add each number to current_sum
# 3. If current_sum becomes bigger than max_sum, update it
# 4. If current_sum becomes negative, reset it to o
# 5. Final max sum is the answer    