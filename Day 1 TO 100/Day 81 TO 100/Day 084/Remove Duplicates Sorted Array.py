# Remove Duplicates Sorted Array

# You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.
# Examples :

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: After removing all the duplicates only one instance of 2 will remain i.e. [2] so modified array will contains 2 at first position and you should return array containing [2] after modifying the array.
# Input: arr[] = [1, 2, 4]
# Output: [1, 2, 4]
# Explation:  As the array does not contain any duplicates so you should return [1, 2, 4].

class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return []
        
        result = [arr[0]]
        
        for i in range(1, len(arr)):
            
            if arr[i] != arr[i-1]:
                
                result.append(arr[i])
        
        return result
    
# Algorithm:
# 1. Check if the input array is empty. If it is, return an empty array.
# 2. Initialize a new array called result with the first element of the input array.
# 3. Iterate through the input array starting from the second element (index 1).
# 4. For each element, compare it with the previous element in the input array.
# 5. If the current element is not equal to the previous element, it means it is a distinct element. Append it to the result array.
# 6. After iterating through the entire input array, return the result array containing only distinct elements.
