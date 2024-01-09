"""
Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list or null. 

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each node has its value set to the value of its 
corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers
in the original list and copied list represent the same state. None of the pointers in the new list should point to nodes in the original list. 

For example, if there are two nodes X and Y in the original list, where X.random -> Y, then the corresponding two nodes x and y in the copied list,
x.random -> y. 

Return the head of the copied linked list. 

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [va;, random_index] where:

- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n - 1) that the random pointer points to, or null if it does not point to any node. 

Your code will only be given the head of the original linked list. 
"""

class Node(object):
    def __init__(self, x, val=0, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    """
    :type head: Node
    :rtype: Node
    """

