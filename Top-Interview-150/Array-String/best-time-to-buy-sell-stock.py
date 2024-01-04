"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith
day. 

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock. 

Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0. 
"""

class Solution(object):
    """
    :type prices: List[int]
    :rtype: int
    """
    maximum_profit = 0
    minimum_profit = float('inf')

    # Sliding window approach

    # Iterate through the array
    # 