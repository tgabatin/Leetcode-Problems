"""
Merge Sorted Array

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order, and 
two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order. 

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accomodate this, nums1 has a length of m + n, where the
first m elements denote the elements that should be merged, and the last n elements
are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in place instead
        """
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
        while j >=0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

"""
Explanation Solution 1:

This solution is solved by using a two-pointer approach. 

Since we need to sort this in order, and we are not using any sort() function intially due to the arrays already being sorted in non-decreasing order, what we can do to merge both of them in place
is to initialize pointers at the end of the respective arrays and compare the elements at array 1 vs. 2. 

"""
    
class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in place
        """
        i, j, k = 0, 0, 0

        nums1_copy = nums1[:m]

        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            nums1[k] = nums1_copy[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1


"""
Explanation Solution 2:

"""