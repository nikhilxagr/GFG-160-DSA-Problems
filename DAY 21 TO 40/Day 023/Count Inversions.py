# Count Inversions

# Given an array of integers arr[]. You have to find the Inversion Count of the array. 
# Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].

# Examples

"""
Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.

Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.

"""

# Solution

class Solution:
    def inversionCount(self, arr):
        def merge_and_count(arr, temp_arr, left, mid, right):
            i = left    
            j = mid + 1 
            k = left    
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1

            for index in range(left, right + 1):
                arr[index] = temp_arr[index]

            return inv_count

        def merge_sort_and_count(arr, temp_arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
                inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
                inv_count += merge_and_count(arr, temp_arr, left, mid, right)

            return inv_count

        n = len(arr)
        temp_arr = [0]*n
        return merge_sort_and_count(arr, temp_arr, 0, n - 1)


# Example
sol = Solution()
print(sol.inversionCount([2, 4, 1, 3, 5]))  


        
