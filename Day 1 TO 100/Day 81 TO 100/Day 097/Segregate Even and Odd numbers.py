# Segregate Even and Odd numbers

# Given an array arr, write a program segregating even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

# Note:- You don't have to return the array, you have to modify it in-place.

# Example:

# Input: arr[] = [12, 34, 45, 9, 8, 90, 3]
# Output: [8, 12, 34, 90, 3, 9, 45]
# Explanation: Even numbers are 12, 34, 8 and 90. Rest are odd numbers.
# Input: arr[] = [0, 1, 2, 3, 4]
# Output: [0, 2, 4, 1, 3]
# Explanation: 0 2 4 are even and 1 3 are odd numbers.
# Input: arr[] = [10, 22, 4, 6]
# Output: [4, 6, 10, 22]
# Explanation: Here all elements are even, so no need of segregataion



class Solution:
    def segregateEvenOdd(self, arr):
        
        even_nums = []
        odd_nums = []

        for value in arr:
            
            if value % 2 == 0:
                even_nums.append(value)
            else:
                odd_nums.append(value)

        even_nums.sort()
        odd_nums.sort()

        i = 0
        
        for value in even_nums:
            arr[i] = value
            i += 1

        for value in odd_nums:
            arr[i] = value
            i += 1