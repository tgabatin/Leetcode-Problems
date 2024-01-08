"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The 
digits are stored in reverse order, and each of their nodes contain a single digit. 
Add the two numbers and return the sum as a linked list. 

You may assume the two numbers do not contain any leading zero, except the number
0 itself. 
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = ListNode()
        curr = result
        carry = 0

        while l1 is not None or l2 is not None: 
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            total = x + y + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return result.next


"""
Explanation Solution 1:


"""