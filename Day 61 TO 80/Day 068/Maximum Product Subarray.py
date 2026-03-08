# Maximum Product Subarray

# Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

# Note: It is guaranteed that the answer fits in a 32-bit integer.

# Examples

# Input: arr[] = [-2, 6, -3, -10, 0, 2]
# Output: 180
# Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.
# Input: arr[] = [-1, -3, -10, 0, 6]
# Output: 30
# Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.
# Input: arr[] = [2, 3, 4] 
# Output: 24 
# Explanation: For an array with all positive elements, the result is product of all elements. 

# Maximum Product Subarray

class Solution:
    def maxProduct(self, arr):
        ans = float('-inf')
        prod = 1
        
        # left to right
        for num in arr:
            prod *= num
            ans = max(ans, prod)
            
            if prod == 0:
                prod = 1
        
        prod = 1
        
        # right to left
        for num in reversed(arr):
            prod *= num
            ans = max(ans, prod)
            
            if prod == 0:
                prod = 1
        
        return ans




# arr = [-2, 6, -3, -10, 0, 2]

# for i in range(1, len(arr)):
#     if arr[i - 1] == 0:
#         continue
#     arr[i] *= arr[i - 1]
    
# print(max(arr))
    