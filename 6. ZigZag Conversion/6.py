class Solution(object):
    def convert(self, s, numRows):
        step = (numRows == 1) - 1  # 0 or -1
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1:
                step = -step  #change direction
            idx += step
        return ''.join(rows)
