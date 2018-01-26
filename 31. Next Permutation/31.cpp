class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // Find from the smallest k such that nums[k - 1] < nums[k].
        int k;
        for (k = nums.size() - 1; k > 0 && nums[k - 1] >= nums[k]; k--);
        
        // k == 0 means the sequence itself is non-increasing. Reverse it.
        if (k > 0) {
            // Find the index i such that nums[i] > nums[k-1], i in [k, n-1].
            int i;
            for (i = nums.size() - 1; nums[i] <= nums[k - 1]; i--);
            
            swap(nums[k - 1], nums[i]);
        }
        reverse(nums.begin() + k, nums.end());
    }
};