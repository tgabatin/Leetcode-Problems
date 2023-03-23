"""
Given the head of a sorted linked list, delete all duplicates such
that each element appears only once. Return the linked list sorted as well.
"""

class ListNode(object):
    def __init__(self, val=0, next=none):
        self.val = val
        self.next = next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None
        
        current = head

        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

