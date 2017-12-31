class Solution(object):
    def myAtoi(self, str):
        import re
        p=re.compile('\\s*([+-]?)(\\d*)')
        n=p.match(str)
        
        if n.group(1)=='-':
            sign = -1
        else:
            sign = 1
            
        number=0
        for i in range (0,len(n.group(2))):
            number=number*10+(ord(n.group(2)[i])-ord('0'))
            
        number=number*sign
        
        if (number>2147483647):
            number=2147483647
        if (number<-2147483648):
            number=-2147483648
        
        return number