"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve
the problem without modifying the values in the list's nodes (i.e., only nodes themselves
may be changed.)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        prev_node = dummy
        curr_node = head

        if curr_node:
            next_node = curr_node.next
        else:
            next_node = None

        while curr_node and next_node:
            next_pair_node = next_node.next

            prev_node.next = next_node
            next_node.next = curr_node
            curr_node.next = next_pair_node

            if curr_node:
                next_node = curr_node.next
            else:
                next_node = None
        
        return dummy.next
