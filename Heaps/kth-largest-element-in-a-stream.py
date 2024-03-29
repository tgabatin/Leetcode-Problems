"""
Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Implement the KthLargest class:
-KthLargest(int k, int[] nums) Initializes the object with the integer k and the 
stream of integers nums
- int add(int val) Appends the integer val to the stream and returns the element
representing the kth largest element in the stream.
"""

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """