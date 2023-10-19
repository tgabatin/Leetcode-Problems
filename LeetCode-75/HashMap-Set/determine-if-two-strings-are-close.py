"""
Determine If Two Strings Are Close

Two strings are considered close if you can attain one string from the other using
the following operations:

- Operation 1: Swap any two existing characters
    - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another
existing character and do the same with the other character. 
    - For example, aacabb -> bbcbaa (all a's turn into b's and all b's turn into a's)

You can use the operations on either string as many times as necessary

Given two strings, word1 and word2, return true if word1 and word2 are close, and
false otherwise. 
"""

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        
        count1 = {}
        count2 = {}

        for char in word1:
            count1[char] = count1.get(char, 0) + 1

        for char in word2:
            count2[char] = count2.get(char, 0) + 1
        
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        if sorted(count1.values()) == sorted(count2.values()):
            return True
        else:
            return False