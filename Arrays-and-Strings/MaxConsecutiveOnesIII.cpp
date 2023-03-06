#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int longestOnes(vector<int> &nums, int k)
    {
        int max_len = 0;
        int zero_count = 0;
        int l = 0;
        int r = 0;
        for (r = 0; r < nums.size(); r++)
        {
            if (nums[r] == 0)
                zero_count++;
            while (zero_count > k)
            {
                if (nums[l++] == 0)
                    zero_count--;
            }
            max_len = max(max_len, r - l + 1);
        }
        return max_len;
    }
};