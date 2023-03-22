"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true
if sentence is a pangram, or false otherwise.
"""

"""
Runtime Complexity: O(n)
Space Complexit: O(1)
"""

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # Create a hash map to store the occurence of the letters
        num_letters = {}
        alphanet_string = 'abcdefghijklmnopqrstuvwxyz'

        for char in sentence:
            if char not in num_letters:
                num_letters[char] = 1
            else:
                num_letters[char] += 1

        for letter in alphanet_string:
            if letter not in num_letters:
                return False
            
        return True