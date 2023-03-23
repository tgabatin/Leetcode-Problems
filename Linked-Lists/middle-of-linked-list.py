"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Runtime Complexity: O(n)
Spacetime Complexity: O(1)
"""
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow