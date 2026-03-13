# Less Than

# You are given a number k and a list arr[] that contains integers. You need to return list of numbers that are less than k.

# Examples:

# Input: arr[] = [54, 43, 2, 1, 5], k = 6
# Output: 2 1 5
# Explanation: 2 1 5 are less than 6.
# Input: arr[] = [5, 6, 7, 2, 4, 8, 9, 1], k = 5
# Output: 2 4 1
# Explanation: 2 4 1 are less than 5.

def lessThan(arr, k):
    ans = []
    for i in arr:
        if i < k:
            ans.append(i)
    return ans