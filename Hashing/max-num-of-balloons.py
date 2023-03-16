"""
Given a string 'text', you want to use the characters of 'text' to form
as many instances of the word 'balloon' as possible. 

You can use each character in 'text' at most once. Return the maximum number 
of instances that can be formed.
"""

class Solution(object):
    def maxNumberOfBalloons(self,text):
        """
        :type text: str
        :rtype: int
        """
        balloon_char = {"b":0, "a":0, "l":0, "n":0}

        for char in text:
            if char in balloon_char:
                balloon_char[char] += 1

        balloon_word = min(balloon_char["b"], balloon_char["a"], balloon_char["l"] // 2, balloon_char["o"] // 2, balloon_char["n"])

        return balloon_word

        