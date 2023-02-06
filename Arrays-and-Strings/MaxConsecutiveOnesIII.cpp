/**
 * @file MaxConsecutiveOnesIII.cpp
 * @author Taylor Sanchez
 * @brief 
 * @version 0.1
 * @date 2023-02-05
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <iostream>
#include <vector>

using namespace std;

/**
 * @brief First Solution - O(n)
 * 
 */
class Solution {
    public:
        int longestOnes(vector<int>& nums, int k) {
            int max_len = 0;
            int zero_counter = 0;
            int l = 0;
            int r = 0;
            for (r = 0; r < nums.size(); r++) {
                if(nums[r] == 0) {
                    zero_counter++;
                }
                while (zero_counter > k) {
                    if (nums[l++] == 0) {
                        zero_counter--;
                    }
                }
            }
            max_len = max(max_len, r - l + 1);
            return max_len;
        }
};