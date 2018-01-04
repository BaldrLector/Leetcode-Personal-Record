class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low,high = 0,len(height)-1
        maximal = 0
        while(low < high):
            temp = (high-low)*min(height[low],height[high])
            if temp > maximal:
                maximal = temp
            if height[low] < height[high]:
                low = low +1
            elif height[low] > height[high]:
                high = high -1
            else:
                low = low+1
                high = high-1
        return maximal