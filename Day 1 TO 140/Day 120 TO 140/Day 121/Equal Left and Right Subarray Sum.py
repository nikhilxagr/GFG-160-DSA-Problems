# Equal Left and Right Subarray Sum

# Given an array arr. The task is to find the first index in the array such that the sum of elements before it is equal to the sum of elements after it. Return -1 if no such point exists.

# Examples :

# Input: arr[] = [1,3,5,2,2] 
# Output: 2 
# Explanation: For second test case at position 2 elements before it (1+3) = elements after it (2+2). 
# Input: arr[] = [1]
# Output: 0
# Explanation: Since its the only element hence it is the only point.
# Input: arr[] = [5, 4, 3, 2, 1]
# Output: -1



class Solution:
    def equalSum(self,arr):
        
        n = len(arr)
        
        lt_sum = 0
        rt_sum = sum(arr)

        for i in range(n):
            rt_sum -= arr[i]

            if lt_sum == rt_sum:
                return i

            lt_sum += arr[i]

        return -1