"""
Search Suggestions System

You are given an array of strings products and a string searchWord. 

Design a system that suggests at most three product names from products after each character
of searchWord is typed. Suggested products should have common prefix with searchWord. If there
are more than three products with a common prefix return the three lexicographically minimums
products.

Returns a list of the suggested products after each character of searchWord is typed.
"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        root = TrieNode()

        for product in sorted(products):
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        result = []
        node = root

        for char in searchWord:
            if char not in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                result.append([])
                node = TrieNode()

        return result