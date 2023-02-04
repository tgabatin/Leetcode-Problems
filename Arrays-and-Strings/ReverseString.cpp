/**
 * @file ReverseString.cpp
 * @author Taylor Sanchez
 * @brief 
 * @version 0.1
 * @date 2023-02-04
 * 
 * @copyright Copyright (c) 2023
 * 
 */

/**
 * @brief Write a function that reverses a string. The input string is given
 * as an array of characters s. You must do this by modifying the input array in-place with O(1)
 * extra memory.
 * 
 * Example 1:
 * Input: s = ["h","e","l","l","o"]
 * Output: ["o","l","l","e","h"]
 * 
 * Example 2:
 * Input: s = ["H","a","n","n","a","h"]
 * Output: ["h","a","n","n","a","H"]
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        void reverseString(vector<char>& s) {
            int left = 0;
            int right = s.size() - 1;
            while (left < right) {
                char temp = s[left];
                s[left] = s[right];
                s[right] = temp;
                left++;
                right--;
            }
        }
};

/**
class Solution1 {
    public:
        void reverseString1 (vector<char>& s) {
            int left = 0, right = s.size() - 1;
            while (left < right) {
                swap(s[left++], s[right--]);
            }
        }
};
*/

/**
class Solution2 {
    public:
        void reverseString2 (vector<char>& s) {
            reverse(s.begin(), s.end());
        }
 * 
 */