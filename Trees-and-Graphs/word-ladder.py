"""
A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to 
be in wordList
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of 
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """