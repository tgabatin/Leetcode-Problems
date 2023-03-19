"""
Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise. 

Each letter in magazine can only be used once in ransomNote.
"""

# Runtime Complexity: O(m+n)
# Spacetime Complexity: O(n)
class Solutionm(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtyope: bool
        """

        magazine_char = {}
        for char in magazine:
            if char in magazine_char:
                magazine_char[char] += 1
            else:
                magazine_char[char] = 1
        
        for char in ransomNote:
            if char not in magazine_char or magazine_char[char] == 0:
                return False
            magazine_char[char] -= 1
        
        return True