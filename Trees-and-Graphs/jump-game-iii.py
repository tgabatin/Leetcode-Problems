"""
Jump Game III

Given an array of non-negative integers arr, you are initially positioned at start
index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i],
check if you can reach to any index with value 0. 

Notice that you can not jump outside of the array at any time.
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
        visited = set()
        visited.add(start)
        
        queue = [start]
        
        while queue:
            curr_index = queue.pop(0)
            
            if arr[curr_index] == 0:
                return True
            
            forward_index = curr_index + arr[curr_index]
            backward_index = curr_index - arr[curr_index]
            
            if 0 <= forward_index < len(arr) and forward_index not in visited:
                visited.add(forward_index)
                queue.append(forward_index)

            if 0 <= backward_index < len(arr) and backward_index not in visited:
                visited.add(backward_index)
                queue.append(backward_index)
        
        # If all nodes have been visited, exit
        return False