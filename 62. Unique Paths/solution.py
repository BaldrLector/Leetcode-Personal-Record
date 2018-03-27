class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[0] * (max(m, n) + 1) for _ in range(max(m, n) + 1)]
        for i in range(1, m + 1):
            f[i][1] = 1
        for i in range(1, n + 1):
            f[1][i] = 1

        for i in range(2, m + 1):
            for j in range(2, n + 1):
                f[i][j] = f[i][j - 1] + f[i - 1][j]

        return f[m][n]
