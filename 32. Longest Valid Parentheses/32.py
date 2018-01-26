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
        