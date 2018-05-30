class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0: return max(m, n)

        table = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): table[i][0] = i
        for j in range(n + 1): table[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if word1[i - 1] == word2[j - 1] else 1
                table[i][j] = min(table[i - 1][j] + 1, table[i][j - 1] + 1, table[i - 1][j - 1] + cost)

        return table[m][n]

# 设dp[i][j]为word1的前i个字符到word2的前j个字符的编辑距离。则状态转移方程为：
# dp[i][j]=min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1] (if(words1[i-1])==words2[j-1]), dp[i-1][j-1] +1(if(words1[i-1])!=words2[j-1]))。其中：

# 1、dp[i][j-1]+1,表示word2插入word2[j]，或者word1删除word1[i]

# 2、dp[i-1][j]+1,表示word2删除word2[j]，或者word1插入word1[i]

# 3、dp[i-1][j-1] (if(words1[i-1])==words2[j-1])，不动即可。

# 4、 dp[i-1][j-1] +1(if(words1[i-1])!=words2[j-1])，最后一个字符替换下。

# 边界条件，dp[i][0]=i， dp[0][j]=j，代码实现如下：

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0: return max(m, n)
        dp= [[0 for i in range(n+1)] for _ in range(m+1)]

        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1, dp[i-1][j-1] if word1[i-1]==word2[j-1] else (dp[i-1][j-1]+1) )
        
        return dp[m][n]