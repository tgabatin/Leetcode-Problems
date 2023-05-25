"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2 - 9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order. 

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
"""

"""
Time Complexity: O(4^n)
Space Complexity: O(n)
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []
        self.dfs(digits, digit_map, 0, '', combinations)
        return combinations

    def dfs(self, digits, digit_map, index, path, combinations):
        if len(path) == len(digits):
            combinations.append(path)
            return

        for letter in digit_map[digits[index]]:
            self.dfs(digits, digit_map, index + 1, path + letter, combinations)
