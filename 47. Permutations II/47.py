class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break  # handles duplication
                        break  # handles duplication
        return ans
        return ans
