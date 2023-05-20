"""
A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to 
be in wordList
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of 
"""

from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([beginWord, 1])
        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level
            
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i + 1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, level + 1))
        
        return 0