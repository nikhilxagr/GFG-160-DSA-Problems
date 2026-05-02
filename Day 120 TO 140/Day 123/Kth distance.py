# Kth distance

# Given an unsorted array arr and a number k which is smaller than the size of the array. Return true if the array contains any duplicate within k distance throughout the array else false.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 1, 2, 3, 4], k = 3
# Output: false
# Explanation: All duplicates are more than k distance away.
# Input: arr[] = [1, 2, 3, 1, 4, 5], k = 3
# Output: true
# Explanation: 1 is repeated at distance 3.
# Input: arr[] = [6, 8, 4, 1, 8, 5, 7], k = 3
# Output: true
# Explanation: 8 is repeated at distance 3.


class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        
        s = set()
        
        for i in range(len(arr)):
            
            if arr[i] in s:
                return True
            
            s.add(arr[i])
            if len(s) > k:
                s.remove(arr[i-k])
                
        return False