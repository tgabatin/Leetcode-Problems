"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the
reversed list.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        if left == right:
            return head
        
        temp = ListNode(0, head)
        prev = temp

        for i in range(left - 1):
            prev = prev.next

        curr = prev.next

        for i in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return temp.next