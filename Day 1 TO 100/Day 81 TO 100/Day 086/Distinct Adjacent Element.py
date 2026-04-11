# Distinct Adjacent Element

# Given an array arr[] of integers, the task is to check whether obtaining an array with distinct adjacent elements is possible by swapping two neighboring array elements.

# Examples:

# Input: arr[] = [1, 1, 2]
# Output: true
# Explanation: Swapping last 2 elements can result in [1, 2, 1].
# Input: arr[] = [7, 7, 7, 7]
# Output: false
# Explanation: We can't swap to obtain distinct elements in neighbor.


class Solution:
    def distinctAdjacentElement(self, arr):
        
        n = len(arr)
        if n <= 1:
            return True

        freq = {}
        
        max_freq = 0

        for value in arr:
            
            freq[value] = freq.get(value, 0) + 1
            
            if freq[value] > max_freq:
                
                max_freq = freq[value]

        return max_freq <= (n + 1) // 2