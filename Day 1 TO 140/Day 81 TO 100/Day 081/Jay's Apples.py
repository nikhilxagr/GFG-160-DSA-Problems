# Jay's Apples

# Given a queue of persons represented by an array of integers, where each person is identified by a specific integer, find the minimum kilograms of apples that need to be distributed, ensuring that each person receives 1 kilogram of apples only once.

# Examples:

# Input: arr[] = [1, 1, 1, 1, 1]
# Output: 1
# Explanation: The person identified by '1' appears multiple times but will only receive 1 kilogram of apples once. Therefore, the minimum apples required is 1 kg.
# Input: arr[] = [1, 2, 3, 1, 2]
# Output: 3
# Explanation: There are three distinct persons in the queue, so 3 kilograms of apples need to be distributed.



class Solution:
    def  minimumApple(self, arr):
       
        ans = set()
        
        for person in arr:
            ans.add(person)

        return len(ans)
    
    
# Example :

obj = Solution()
arr = [1, 1, 1, 1, 1]

print(obj.minimumApple(arr))

# Algorithm:
# 1. Initialize an empty set to store unique person identifiers.
# 2. Iterate through the input array and add each person identifier to the set.
# 3. The size of the set will give the count of unique persons, which is the minimum kilograms of apples needed.
