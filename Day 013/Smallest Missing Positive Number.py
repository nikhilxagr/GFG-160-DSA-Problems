# Problem Statement:

# Smallest Missing Positive Number


# You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

# Examples:
"""
Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.
Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.
Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1.
"""

# Solution:

# Approach:
# 1. We can use a set to store all the positive numbers in the array.
# 2. Then, we can iterate from 1 to the length of the array + 1 and check if each number is in the set.
# 3. The first number that is not found in the set is the smallest missing positive number.

class Solution:
    def missingNumber(self, arr):
        positive_nums = set()
        
        # Store all positive numbers in the set
        for num in arr:
            if num > 0:
                positive_nums.add(num)
        
        # Find the smallest missing positive number
        smallest_missing = 1
        while True:
            if smallest_missing not in positive_nums:
                return smallest_missing
            smallest_missing += 1
            
if __name__ == "__main__":
    solve = Solution()
    
    arr1 = [2, -3, 4, 1, 1, 7]
    print(solve.missingNumber(arr1))
    
    arr2 = [5, 3, 2, 5, 1]
    print(solve.missingNumber(arr2)) 
    
    arr3 = [-8, 0, -1, -4, -3]
    print(solve.missingNumber(arr3)) 