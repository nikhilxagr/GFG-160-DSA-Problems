# Move all negative elements to end

# Given an unsorted array arr[ ] having both negative and positive integers. The task is to place all negative elements at the end of the array without changing the order of positive elements and negative elements.

# Note: Don't return any array, just in-place on the array.

# Examples:

# Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
# Output : [1, 3, 2, 11, 6, -1, -7, -5]
# Explanation: By doing operations we separated the integers without changing the order.

# Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
# Output : [7, 9, 10, 11, -5, -3, -4, -1]



class Solution:
    def segregateElements(self, arr):
        pos = []
        neg = []
        ans = []

        for num in arr:
            
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
                
        result = pos + neg
        return result



# arr = [1, -1, 3, 2, -7, -5, 11, 6]
# pos = []
# neg = []
# ans = []

# for num in arr:
    
#     if num >= 0:
#         pos.append(num)
#     else:
#         neg.append(num)
        
# result = pos + neg
# print(result)