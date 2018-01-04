class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 5000: ''}
        dividor = 1000
        out = ''
        while num:
            x, num = divmod(num, dividor)
            if x == 9 or x == 4:
                out += table[dividor] + table[dividor * (x + 1)]
            else:
                a, b = divmod(x, 5)
                out += table[dividor * 5] * a + table[dividor] * b
            dividor //= 10
        return out