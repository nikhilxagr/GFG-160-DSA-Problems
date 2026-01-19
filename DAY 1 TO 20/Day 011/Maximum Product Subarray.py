# Problem Statement:

# Maximum Product Subarray

# Given an array arr[] consisting of positive, negative, and zero values, find the maximum product that can be obtained from any contiguous subarray of arr[].

# Note: It is guaranteed that the answer fits in a 32-bit integer.

"""Examples:

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.

Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 
"""

# Solution:

class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        currMax = arr[0]
        currMin = arr[0]
        maxProduct = arr[0]

        for i in range(1, n):
            
            temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)
            
            currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)
            
            currMax = temp
            
            maxProduct = max(maxProduct, currMax)

        return maxProduct
    
if __name__ == "__main__":
    solution = Solution()
    arr1 = [-2, 6, -3, -10, 0, 2]
    print(solution.maxProduct(arr1)) 