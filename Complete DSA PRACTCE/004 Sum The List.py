# Sum The List

# You are given a list that contains integers. You need to return the sum of the list.

# Examples:

# Input: arr = [54, 43, 2, 1, 5]
# Output: 105
# Explanation: Just sum it 54 + 43 + 2 + 1 + 5 = 105.
# Input: arr = [324, 5, 2, 2]
# Output: 333
# Explanation: Just sum it 324 + 5 + 2 + 2 = 333. 

def listSum(arr):
    sum = 0
    
    for i in range(len(arr)):
        
        sum += arr[i]
        
    return sum