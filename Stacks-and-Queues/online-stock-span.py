"""
Design an algorithm that collects daily price quotas for some stock and returns
the span of that stock's price for the current day. 

The span of the stock's price in one day is the maximum number of consecutive days
(starting from that day and going backward) for which the stock price was less than or equal
to that price of the day.

- For example, if the prices of the stock in the last four days is [7,2,1,2] and the price 
of the stock today is 2, then the span of today is 4 because starting from today, the price 
of the stock was less than or equal to 2 for 4 consecutive days. 
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price:int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span