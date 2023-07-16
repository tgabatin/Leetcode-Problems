"""
Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k. 

Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than 10^-5
will be accepted.
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)

        return float(max_sum) / k

        