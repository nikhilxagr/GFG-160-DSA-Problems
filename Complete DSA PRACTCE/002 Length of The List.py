# Length of The List

# You are given a list that contains integers. You need to return the length of the list.

# Examples:

# Input: arr = [54, 43, 2, 1, 5]
# Output: 5
# Explanation: The list contains 5 elements so its length is 5.
# Input: arr = [324, 5, 2, 2]
# Output: 4
# Explanation: The list contains 4 elements so its length is 4. 

def listLength(arr):
    count = 0
    for i in arr:
        count += 1
    return count