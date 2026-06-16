# Merging two unsorted arrays in sorted order

# Given two different arrays arr1[] and arr2[], the task is to merge the two unsorted arrays and return a sorted array.

# Examples:

# Input: arr1[] = [10, 5, 15] , arr2[] = [20, 3, 2]
# Output: [2, 3, 5, 10, 15, 20]
# Explanation: After merging both the array's and sorting it with get the desired output.  
# Input: arr1[] = [1, 10, 5, 15] , arr2[] = [20, 0, 2]
# Output: [0, 1, 2, 5, 10, 15, 20]
# Expected Time Complexity: O (nlogn + mlogm + (n + m))
# Expected Auxiliary Space: O(n+m)

class Solution:
    def sortedMerge(self, arr1,arr2,res):
        
        arr1.sort()
        arr2.sort()
        i = j = k = 0
        
        while i < len(arr1) and j < len(arr2):
            
            if arr1[i] < arr2[j]:
                res[k] = arr1[i]
                i += 1
            else:
                res[k] = arr2[j]
                j += 1
            k += 1
            
        while i < len(arr1):
            res[k] = arr1[i]
            i += 1
            k += 1
            
        while j < len(arr2):
            res[k] = arr2[j]
            j += 1
            k += 1