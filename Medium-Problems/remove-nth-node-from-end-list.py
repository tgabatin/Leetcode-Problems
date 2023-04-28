"""
Remove Nth Node From End of List

Description:
Given the head of a linked list, remove the nth node from the end of the list
and return its head.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Utilization of two pointers
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next 
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
    
        return head