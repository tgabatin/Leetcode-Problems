"""
You are given an integer array matches where mathces[i] = [winner_i, loser_i]
indicates that the player winer_i defeated player loser_i in a math.

Return a list answer of size 2 where:
    - answer[0] is a list of all the players that have not lost any mathces
    - answer[1] is a list of all players that hve lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:
    - You should only consider the players that have played at least one match.
    - The testcases will be generated such that no two matches will have the same outcome.  
"""


# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]  #Technically a double array
        :rtype: List[List[int]] # Technically a double array
        """
        wins = {}
        losses = {}

        for match in matches:
            winner = match[0]
            loser = match[1]

            if winner not in wins:
                wins[winner] = 0
            wins[winner] += 1

            if loser not in losses:
                losses[loser] = 0
            losses[loser] += 1

        no_losses = sorted([player for player in wins if player not in losses])
        one_loss = sorted([player for player in losses if losses[player] == 1])

        return [no_losses, one_loss]


        
