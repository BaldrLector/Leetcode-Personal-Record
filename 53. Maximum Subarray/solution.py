class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub,fn=nums[0],0
        for i in nums:
            fn=max(i,fn+i)
            max_sub=max(max_sub,fn)
        return max_sub