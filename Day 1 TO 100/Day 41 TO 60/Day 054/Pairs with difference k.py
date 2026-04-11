# Pairs with difference k

# Given an array arr[] of positive integers. Find the number of pairs of integers whose absolute difference equals to a given number k.
# Note: (a, b) and (b, a) are considered the same. Also, the same numbers at different indices are considered different.

# The answer is guaranteed to fit in a 32-bit integer.

# Examples:

# Input: arr[] = [1, 4, 1, 4, 5], k = 3
# Output: 4
# Explanation: There are 4 pairs with absolute difference 3, the pairs are {1, 4}, {1, 4}, {4, 1} and {1, 4}.

# Input: arr[] = [8, 16, 12, 16, 4, 0], k = 4
# Output: 5
# Explanation: There are 5 pairs with absolute difference 4, the pairs are {8, 12}, {8, 4}, {16, 12}, {12, 16}, {4, 0}.

# class Solution:
#     def countPairs(self, arr, k):
        
#         ans = 0
#         for i in range(len(arr)):
            
#             for j in range(i + 1, len(arr)):
                
#                 if abs(arr[i] - arr[j]) == k:
                    
#                     ans = ans + 1
#         return ans

# optimized approach
class Solution:
    def countPairs(self, arr, k):
        count = 0
        freq = {}
        
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in arr:
            if num + k in freq:
                count += freq[num + k]
        
        return count

# arr = [1, 4, 1, 4, 5]
# k = 3

# ans = 0
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
        
#         if abs(arr[i] - arr[j]) == k:  # Check if the absolute difference is equal to k
#             print(f"({arr[i]}, {arr[j]})")
            
#             ans = ans + 1
# print(ans)