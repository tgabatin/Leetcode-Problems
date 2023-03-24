/**
 * @file SquaresOfASortedArray.cpp
 * @author Taylor Sanchez
 * @brief 
 * @version 0.1
 * @date 2023-02-04
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        vector<int> sortedSquares(vector<int>& nums) {
            vector<int> result;
            for(int i = 0; i < nums.size(); i++) {
                result.push_back(nums[i] * nums[i]);
            }
            sort(result.begin(), result.end());
            return result;
        }
};