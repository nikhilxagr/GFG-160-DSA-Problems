# Largest subarray of 0's and 1's

# Examples:

# Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
# Output: 6
# Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
# Input: arr[] = [0, 0, 1, 1, 0]
# Output: 4
# Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
# Input: arr[] = [0]
# Output: 0
# Explnation: There is no subarray with an equal number of 0s and 1s.

# Solution:
 
class Solution:
    def maxLen(self, arr):
        prefix_sum = 0
        max_len = 0
        index_map = {0: -1}  # prefix_sum : first index
        
        for i in range(len(arr)):
            if arr[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            if prefix_sum in index_map:
                max_len = max(max_len, i - index_map[prefix_sum])
            else:
                index_map[prefix_sum] = i
        
        return max_len
