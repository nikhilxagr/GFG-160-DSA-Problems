# Who has the majority

# Given an array arr[] and two elements x and y, return the element that occurs more frequently. If both elements have the same frequency, return the smaller one.

# Examples:

# Input: arr[] = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5], x = 4, y = 5
# Output: 4
# Explanation: frequency of 4 is 4.frequency of 5 is 1.Since 4>1 so return 4
# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], x = 1, y = 7
# Output: 1
# Explanation: frequency of 1 is 1.frequency of 7 is 1.Since 1 < 7, return 1.

class Solution:
    def moreFrequent(self, arr, x, y):
        
        count1 = arr.count(x)
        count2 = arr.count(y)

        if count1 > count2:
            return x
        
        elif count2 > count1:
            return y
        
        else:
            return min(x, y)