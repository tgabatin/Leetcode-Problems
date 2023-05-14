"""
1047. Remove All Adacent Duplicates in String

You are given a string s consisting of lowercase English letters. A duplicate removal
consists of choosing two adjacent and equal letters and removing them. 

We repeatedly make duplicate removals on s until we no longer can. 

Return the final string after all such duplicate removals have been made. It can 
be proven the answer is unique.
"""

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """