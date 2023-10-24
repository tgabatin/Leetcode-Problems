"""
Max Number of K-Sum Pairs

You are given an integer array nums and an integer k. 

In one operation, you can pick two numbers from the array whose sum equals k and 
remove them from the array. 

Return the maximum number of operations you can perform on the array.
"""

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}  # Dictionary to store the count of each number
        max_operations = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in nums:
            if count.get(num, 0) > 0 and count.get(k - num, 0) > 0:
                if num == k - num:
                    pairs = count[num] // 2
                else:
                    pairs = min(count[num], count[k - num])
                max_operations += pairs
                count[num] -= pairs
                count[k - num] -= pairs

        return max_operations



        
# Thought Process
        # Iterate through the list with both pointers initialized at start
        # Keep the first pointer at start and move the second
        # Add the nums at the iteration
        # Check if it equals the number k
        # If it doesn't equal continue
        # If equals, increate 'max_iterations'
        # Remove the items that the pointers are pointed to
        # Start the iteration again
        # If there are no more items and the pointers have reached the end exit
        # Return the max_iterations
