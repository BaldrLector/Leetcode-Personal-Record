class Solution:
    def reverse(self, x):
            """
            :type x: int
            :rtype: int
            """
            sign = lambda x: x and (1, -1)[x < 0]
            r = int(str(sign(x)*x)[::-1])
            return (sign(x)*r, 0)[r > 2**31 - 1]
