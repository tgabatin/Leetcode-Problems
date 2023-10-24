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
        ptr_1 = 0
        ptr_2 = 0
        max_operations = 0

        while ptr_1 < len(nums) - 1 and ptr_2 < len(nums):
            current_sum = nums[ptr_1] + nums[ptr_2]

            if current_sum == k:
                max_operations += 1
                nums.pop(ptr_2)
                nums.pop(ptr_1)
                ptr_2 = ptr_1 + 1
            else:
                ptr_2 += 1
                
            # Check to see if pointer has reached end
            if ptr_2 >= len(nums):
                ptr_1 += 1
                ptr_2 = ptr_1 + 1
                
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
