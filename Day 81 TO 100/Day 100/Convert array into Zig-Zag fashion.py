# Convert array into Zig-Zag fashion

# Given an array arr of distinct elements, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

# arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 

# Note: Modify the given arr[] only, If your transformation is correct, the output will be "true" else the output will be "false". 

# Examples

# Input: arr[] = [4, 3, 7, 8, 6, 2, 1]
# Output: true
# Explanation:  After modification the array will look like 3 < 7 > 4 < 8 > 2 < 6 > 1, the checker in the driver code will produce 1.

# Input: arr[] = [4, 7, 3, 8, 2]
# Output: true
# Explanation: After modification the array will look like 4 < 7 > 3 < 8 > 2 hence output will be 1.

# Input: arr[] = [2, 8, 1, 7, 5, 9]
# Output: true
# Explanation: After modification the array will look like 2 < 8 > 1 < 7 > 5 < 9, the checker in the driver code will produce 1.


from typing import List


class Solution:
    def zigZag(self, arr: List[int]) -> None:
        
        # flag = True means arr[i] should be less than arr[i + 1]
        
        flag = True

        for i in range(len(arr) - 1):
            
            if flag:
                if arr[i] > arr[i + 1]:
                    
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    
            else:
                if arr[i] < arr[i + 1]:
                    
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

            flag = not flag