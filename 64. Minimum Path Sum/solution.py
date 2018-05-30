class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        return dp[-1][-1]

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        dp = [ [0 for _ in range(n)] for i in range(m) ]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]

        for i in range(1,n):
            dp[0][i]=dp[0][i-1]+grid[0][i]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) +grid[i][j]
        
        return dp[m-1][n-1]