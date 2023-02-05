/**
 * @file MaxAvgSubarray.cpp
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

/**
 * @brief 
 * You are given an integer array of nums consisting of n elements, and an integer k.
 * 
 * Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
 * Any answer with a calculation error less than 10-5 will be accepted.
 */


/**
 * @brief Solution 1 - O(n)
 * 
 */
class Solution {
    public:
        double findMaxAverage(vector<int>& nums, int k) {
            int sum = 0;
            for (int i = 0; i < k; i++) {
                sum += nums[i];
            }
            int maxSum = sum;
            for (int i = k; i < nums.size(); i++) {
                sum += nums[i] - nums[i - k];
                maxSum = max(maxSum, sum);
            }
            return maxSum / (double) k;
        }
};