"""
Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the
array. 

Note that it is the kth largest element in the sorted order, not the kth distinct
element. 

Can you solve it without sorting?
"""

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_heap = []

        for num in nums:
            negated_num = -num
            max_heap.append(negated_num)

        heapq.heapify(max_heap)

        for _ in range(k - 1):
            heapq.heappop(max_heap)

        return -max_heap[0]
    

import queue

class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        priority_queue = queue.PriorityQueue()

        for num in nums:
            priority_queue.put(num)
            if priority_queue.qsize() > k:
                priority_queue.get()

        return priority_queue.get()