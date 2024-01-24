"""
Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked
list is known as the twin of the (n - 1 - i)th node, if 0 <= i <= (n / 2) - 1.

- For example, if n = 4, then node 0 is the twin node of 3, and node 1 is the
twin of node 2. These are only nodes with twins for n = 4. 

The twin sum is defined as the sum of a node and its twin. 

Given the head of a linked list with an even length, return the maximum twin sum
of the linked list.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow, fast = head, head

        max_val = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr, prev = slow, None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        while prev:
            max_val = max(max_val, head.val + prev.val)
            prev = prev.next
            head = head.next

        return max_val