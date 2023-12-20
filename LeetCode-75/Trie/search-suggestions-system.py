"""
Search Suggestions System

You are given an array of strings products and a string searchWord. 

Design a system that suggests at most three product names from products after each character
of searchWord is typed. Suggested products should have common prefix with searchWord. If there
are more than three products with a common prefix return the three lexicographically minimums
products.

Returns a list of the suggested products after each character of searchWord is typed.
"""

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """