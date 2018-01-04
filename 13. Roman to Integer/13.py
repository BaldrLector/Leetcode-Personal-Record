class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
     
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res, i = 0, 0
        for i in range(len(s)):
            curr, nxt = s[i], s[i+1:i+2]
            if nxt and roman[curr] < roman[nxt]:
                res -= roman[curr]
            else:
                res += roman[curr]
        return res