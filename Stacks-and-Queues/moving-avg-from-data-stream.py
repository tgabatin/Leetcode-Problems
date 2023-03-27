"""
Given a stream of integers and a window size, calculate the moving average
of all integers in the sliding window. 

Implement the MovingAverage class:

- MovingAverage(int size) Initializes the object with a size of the window size
- double next (int val) Returns the moving average of the last size values of the stream
"""

"""
Time Complexity: O(1)
Space Complexity: O(1)
"""

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.sum -= self.window[0]
            self.window.pop(0)
        self.window.append(val)
        self.sum += val

        return self.sum / len(self.window)