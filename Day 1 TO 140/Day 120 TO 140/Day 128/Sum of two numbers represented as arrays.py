# Sum of two numbers represented as arrays

# Given two numbers represented by two different arrays, arr1[] and arr2[], the task is to find their sum as a new array. Each array represents a number where each element corresponds to a digit in that number. The resulting sum array should also represent the sum of the two numbers in the same digit-by-digit format.

# Note: No leading zeroes in array arr1 and arr2.

# Examples:

# Input: arr1[] = [5, 6, 3], arr2[] = [8, 4, 2]
# Output: [1, 4, 0, 5]
# Explanation: As 563 + 842 = 1405.
# Input: arr1[] = [2, 2, 7, 5, 3, 3], arr2[] = [4, 3, 3, 8]
# Output: [2, 3, 1, 8, 7, 1]
# Explanation: As 227533 + 4338 = 231871.


class Solution:
    def findSum(self, arr1, arr2):

        i = len(arr1) - 1
        j = len(arr2) - 1
        
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            sum_value = carry

            if i >= 0:
                sum_value += arr1[i]
                i -= 1

            if j >= 0:
                sum_value += arr2[j]
                j -= 1

            result.append(sum_value % 10)
            
            carry = sum_value // 10

        return result[::-1]