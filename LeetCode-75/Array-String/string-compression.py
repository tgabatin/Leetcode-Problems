"""
String Compression

Given an array of characters chars, compress it using the following algorithm:

Being with an empty string s. For each group of consecutive repeating characters in
chars:

- If the group's length is 1, append the character to s
- Otherwise, append the character followed by the group's length

The compressed string s should not be returned separately, but instead, be stored in
the input character array chars. Note that the group lengths that are 10 or longer
will be split into multiple characters in chars. 

After you are done modifying the input array, return the new length of the array. 

You must write an algorithm that uses only constant extra space.
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        s = []
        count = 1
        
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i-1]:
                count += 1
            else:
                s.append(chars[i-1])
                if count > 1:
                    count_str = str(count)
                    for digit in count_str:
                        s.append(digit)
                count = 1

        del chars[:]
        chars.extend(s)
        return len(chars)
