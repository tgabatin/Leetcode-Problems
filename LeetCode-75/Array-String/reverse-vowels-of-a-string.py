"""
Reverse Vowels of a String

Given a string s, reverse only all the vowwels in the string and return it. 

The vowels are 'a', 'e', 'i', 'o' and 'u', and they can appear in both
lower and upper cases, more than once.
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        char_list = list(s)
        left = 0
        right = len(char_list) - 1

        while left <= right:
            if char_list[left].lower() not in vowels:
                left += 1
            elif char_list[right].lower() not in vowels:
                right -= 1
            else:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
        
        return ''.join(char_list)