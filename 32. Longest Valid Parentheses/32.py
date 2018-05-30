class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        """ as the ")" will not effect the final result, which acts as a dummy  element to
            make the all the  original elements of s equivalently, 
            otherwise the first element needs to be dealt with separately. 
        """ 
        s = ")" + s  
        stack, ans = [], 0
        for index in range(len(s)):
          element = s[index]
          if element == ")" and stack and stack[-1][1] == "(":
            stack.pop()
            ans = max(ans, index - stack[-1][0])
          else:
            stack.append((index, element))
        return ans

# dp version

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[0 for _ in range(len(s))]
        maxn=0

        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i>=2 else 0) +2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1] =='(':
                    dp[i] = dp[i-1] + ( dp[i-dp[i-1]-2] if i-dp[i-2]>=2 else 0) +2

                maxn = max(maxn,dp[i])
        return maxn