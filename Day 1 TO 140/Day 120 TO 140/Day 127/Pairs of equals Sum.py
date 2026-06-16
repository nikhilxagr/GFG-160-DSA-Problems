# Pairs of equals Sum

# Given an array arr. Find if there are two pairs (a, b) and (c, d) such that a+b = c+d.

# Examples:

# Input: arr[] = [3, 4, 7, 1, 2, 9, 8] 
# Output: true
# Explanation: (3, 7) and (9, 1) are the pairs whosesum are equal.  
# Input: arr[] = [65, 30, 7, 90, 1, 9, 8]
# Output: false
# Explanation: There is no pair.



class Solution:
    def findPairs(self, arr):
        
        sum_dict = {}
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                
                pair_sum = arr[i] + arr[j]
                
                if pair_sum in sum_dict:
                    return True
                
                sum_dict[pair_sum] = (arr[i], arr[j])
                
        return False