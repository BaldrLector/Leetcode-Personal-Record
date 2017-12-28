class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        HashTabel={}
        for index,num in enumerate(nums):
            if target-num in HashTabel:
                return [HashTabel[target-num],index]
            else:
                HashTabel[num]=index
                