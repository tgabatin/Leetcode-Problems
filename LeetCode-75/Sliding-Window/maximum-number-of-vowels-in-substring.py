"""
Maximum Number of Vowels in a Substring of a Given Length

Given a string s and integer k, return the maximum number of vowel letters in any
substring of s with length k. 

Vowel letters in English 'a', 'e', 'i', 'o', 'u'. 

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowels letters. 

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet", and "ode" contain 2 vowels.
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """