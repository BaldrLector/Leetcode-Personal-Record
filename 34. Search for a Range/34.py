class Solution:
       def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        l=0
        r=len(nums)-1

        while l<=r and l<len(nums)-1 and r>0:
            if nums[l]!=target:
                l+=1
            if nums[r]!=target:
                r-=1
            if nums[l]==target and nums[r]==target:
                break
        if nums[l]==target:
            return [l,r]
        else:
            return [-1,-1]
        