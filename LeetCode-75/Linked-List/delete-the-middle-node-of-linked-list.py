"""
Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head
of the modified linked list. 

The middle node of a linked list of size n is the [n / 2]th node from the start using
0-based indexing, where [x] denotes the largest integer less than or equal to x. 

- For n = 1,2,3,4, and 5, the middle nodes are 0,1,1,2, and 2, respectively.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head
        prev = None

        # Traverse the list with fast and slow pointers
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # At this point, slow points to the middle node
        # Remove the middle node
        if prev:
            prev.next = slow.next
        else:
            # If prev is None, it means we are removing the head node
            head = head.next

        return head

        
