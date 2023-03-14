"""
Given an integer array nums, return the largest integer that only occurs once. 
If no integer occurs once, return -1.
"""

# Runtime Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create the Dictionary
        num_occurences = {}
        # Iterate through the value in the integer array nums
        for num in nums:
            if num not in num_occurences: # If the number is not in the occurences
                num_occurences[num] = 0 # Set the value of this to 0
            num_occurences[num] += 1 # Increment the value of the key

        unique_max_num = -1 # Set the initial value of the maximum value while the iteration continues

        # Iterate through the keys within the dictionary
        for key in num_occurences: 
            if num_occurences[key] == 1 and key > unique_max_num: # Checks to see whether the number of occurences is only 1 and the key is currently the max val
                unique_max_num = key # Set the key to be the max val

        # Return the max val
        return unique_max_num

