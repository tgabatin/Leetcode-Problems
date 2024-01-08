"""
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2. 

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. 

Return the head of the merged linked list. 
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        """
        # Create a variable to hold the new result
        result = ListNode(0)
        curr_node = result
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next

            curr_node = curr_node.next

        # Consider the remaining elements
        if list1 is not None:
            curr_node.next = list1
        elif list2 is not None:
            curr_node.next = list2

        return result.next