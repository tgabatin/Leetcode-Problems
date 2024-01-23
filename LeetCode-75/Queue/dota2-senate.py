"""
Dote2 Senate

In the wold of Dota2, there are two parties: the Radiant and the Dire. 

The Dota2 senate consists of senators coming from two parties. Now the Senate wants
to decide on a change in the Dota2 game. The voting for this change is a round-based
procedure. In each round, each senator can exercise one of the two rights:

- Ban one senator's right: A senator can make another senator lose all his rights in
this and the following rounds. 
- Announce the victory: If this senator found the senators who still have rights to 
vote are all from the same party, he can announce the victory and decide on the 
change in the game. 

Given a string senate representing each senator's part belonging. The character 'R'
and 'D' represent the Radiant party and the Dire party. Then if there are n
senators, the size of the given string will be n. 

The round-based procedure starts from the first senator to the last senator in the
given order. This procedure will last until the end of voting. All the senators
who have lost their rights will be skipped during the procedure. 

Suppose every senator is smart enough and will play the best strategy for his own
party. Predict which party will finally announce the victory and change the Dota2
game. The output should be "Radiant" or "Dire". 
"""

import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        ban_count = {'R': 0, 'D': 0}
        senators_queue = deque()

        for i in range(len(senate)):
            senators_queue.append(senate)

        while ban_count['R'] < len(senate) and ban_count['D'] < len(senate):
            current_senator = senators_queue.popleft()

            if ban_count[current_senator] > 0:
                ban_count[current_senator] -= 1
                continue

            if current_senator == 'R':
                ban_count['D'] += 1
            else:
                ban_count['R'] += 1

            senators_queue.append(current_senator)

        return "Radiant" if ban_count['R'] < len(senate) else "Dire"