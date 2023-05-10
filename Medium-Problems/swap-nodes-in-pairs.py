"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve
the problem without modifying the values in the list's nodes (i.e., only nodes themselves
may be changed.)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        