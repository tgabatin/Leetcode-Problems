"""
Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row. 

For each asteroid, the absolute value represents its size, and the sign represents
its direction (positive meaning right, negative meaning left). Each asteroid moves 
at the same speed. 

Find out the state of the asteroids after all collisions. If two asteroids meet, the
smaller one will explode. If both are the same size, both will explode. Two asteroids
moving in the same direction will never meet. 
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)

        return stack

"""
Explanation:


"""