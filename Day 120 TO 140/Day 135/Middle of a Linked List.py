# Middle of a Linked List

# You are given the head of a linked list, You have to return the value of the middle node of the linked list.

# If the number of nodes is odd, return the middle node value.
# If the number of nodes is even, there are two middle nodes, so return the second middle node value.
# Examples:

# Input: 
   
# Output: 3
# Explanation: The given linked list is 1->2->3->4->5 and its middle is 3.
   
# Input:
   
# Output: 7 
# Explanation: The given linked list is 2->4->6->7->5->1 so, there are two middle node 6 and 7, return the second middle node as 7.
   
   
class Solution:
    def getMiddle(self, head):
        
        if head is None:
            return -1
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data