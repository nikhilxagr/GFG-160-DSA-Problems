# Form largest number from digits



# Given an array arr[] of numbers from 0 to 9. Your task is to rearrange elements of the array such that after combining all the elements of the array, the number formed is maximum.

# Examples:

# Input: arr[] = [9, 0, 1, 3, 0]
# Output: 93100
# Explanation: Largest number is 93100 which can be formed from array digits.
# Input: arr[] = [1, 2, 3]
# Output: 321


class Solution:
    def MaxNumber(self, arr):
       
        arr.sort(reverse=True)
        
        return ''.join(str(x) for x in arr)