"""
Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude 
equals 0. 

You are given an integer array gain of length n where gain[i] is the net gain in
altitude between points i and i + 1 for all (0 <= i < n). Return the higest altitude
of a point.
"""

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest_altitude = 0
        current_altitude = 0

        for altitude_gain in gain:
            current_altitude += altitude_gain
            if current_altitude > highest_altitude:
                highest_altitude = current_altitude

        return highest_altitude
