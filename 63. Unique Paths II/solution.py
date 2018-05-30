# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
#         if obstacleGrid[0][0] == 1: return 0
#         for i in range(len(obstacleGrid)):
#             for j in range(len(obstacleGrid[0])): 
#                 if obstacleGrid[i][j] == 1 or i == j == 0:
#                     obstacleGrid[i][j] -= 1
#                 else:
#                     add1 = obstacleGrid[i - 1][j] if i > 0 else 0
#                     add2 = obstacleGrid[i][j - 1] if j > 0 else 0
#                     obstacleGrid[i][j] += add1 + add2
#         return abs(obstacleGrid[-1][-1])

#dp version
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [ [0 for _ in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        dp[0][0] =1;
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0] ==1:
            return 0
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                dp[i][0]=0
            else:
                dp[i][0] = dp[i-1][0]
        for i in range(1,n):
            if obstacleGrid[0][i] ==1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] ==1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ResGrid = [[0 for x in range(n+1)] for x in range(m+1)]
        ResGrid[0][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:
                    ResGrid[i][j] = ResGrid[i][j-1]+ResGrid[i-1][j]

        return ResGrid[m][n]