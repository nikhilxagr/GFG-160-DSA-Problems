# Numbers containing 1, 2 and 3

# You are given an array arr[] of integers. Find all the numbers in the array whose digits consist only of [1, 2, 3].Return an array containing only those numbers from arr[]. The order of the numbers in the output array should be the same as their order in the input array.
# If there is no such element in arr[]. Return [-1].

# Examples:

# Input: arr[] = [4, 6, 7]
# Output: [-1]
# Explanation: No elements are there in the array which contains digits 1, 2 or 3.
# Input: arr[] = [1, 2, 13, 4] 
# Output: [1, 2, 13]
# Explanation: 1, 2 and 13 are the only elements in the array which contains digits as 1, 2 or 3.

class Solution:
    def filterByDigits(self, arr):
        result = []

        for num in arr:
            
            numStr = str(num)
            present = True

            for ch in numStr:
                
                if ch != '1' and ch != '2' and ch != '3':
                    present = False
                    break

            if present:
                result.append(num)

        if len(result) == 0:
            return [-1]
        
        return result