"""
Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array. 

The pivot index is the index where the sum of all of the numbers strictly to the left
of the index is equal to the sum of all of the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are
no elements to the left. This also applies to the right edge of the array. 

Return the leftmost pivot index. If no such index exists, return -1
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot_index = -1 

        total_sum = sum(nums)

        left_sum = 0 

        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num

            if left_sum == right_sum:
                pivot_index = i
                break

            left_sum += num

        return pivot_index 