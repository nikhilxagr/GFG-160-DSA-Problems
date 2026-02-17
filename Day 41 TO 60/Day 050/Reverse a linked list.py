# Reverse a linked list


# You are given the head of a singly linked list. You have to reverse the linked list and return the head of the reversed list.

# Examples:

# Input:
      
# Output: 4 -> 3 -> 2 -> 1
# Explanation: After reversing the linkedList
      
# Input: 
      
# Output: 8 -> 9 -> 10 -> 7 -> 2
# Explanation: After reversing the linked list
      
# Input: 
      
# Output: 8
# Explanation: After reversing the linked list

class Solution:
    def reverseList(self, head):
        prev = None
        Current = head
        while Current:
            
            next_node = Current.next
            Current.next = prev
            prev = Current
            Current = next_node
            
        return prev