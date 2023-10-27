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
        # Check to see if a list exists
        if not head:
            return None
        
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        middle_index = count // 2

        current = head
        prev = None
        index = 0

        while current:
            if index == middle_index:
                if prev:
                    prev.next = current.next
                else:
                    head = head.next
                break

        prev = current
        current = current.next
        index += 1

        return head
        
        # Determine the middle of 'head' and floor the output
        # Iterate through the linked list up to the point of removal
        # Remove the node at the point
        # Return the new linked list 
        

        
