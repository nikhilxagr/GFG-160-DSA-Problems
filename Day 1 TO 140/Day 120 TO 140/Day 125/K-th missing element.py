# K-th missing element

# Given an increasing sequence arr, we need to find the K-th smallest missing element, taking the first element of the array as the starting point in the increasing sequence. If there is no k-th missing element then output -1.

# Example:

# Input: arr[] = [1, 3, 4, 5, 7] and k = 2
# Output: 6
# Explanation: k = 2, Missing numbers are 2 and 6. So 2nd missing number is 6.
# Input: arr[] = [2, 3, 4, 5, 6, 8] and k = 1
# Output: 7
# Explanation: k = 1, the first missing number in the array is 7.
# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(1).

class Solution:
    def KthMissingElement(self,arr,k) :


        missing = 0
        
        for i in range(1, len(arr)):
            
            missing += arr[i] - arr[i-1] - 1
            
            if missing >= k:
                return arr[i-1] + (k - (missing - (arr[i] - arr[i-1] - 1)))
            
        return -1