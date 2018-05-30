class Solution(object):
    def isScramble(self, s1, s2):
        self.records = {}
        return self.recur(s1, s2)
        
    def recur(self, s1, s2):
        if (s1, s2) in self.records:
            return self.records[s1, s2]
        
        if len(s1) == 1:
            return s1 == s2
         
        for i in range(1, len(s1)):
            if (self.recur(s1[0:i], s2[0:i]) and self.recur(s1[i:], s2[i:])) or (self.recur(s1[0:i], s2[-1 * i :]) and self.recur(s1[i:], s2[0: len(s2) - i])) :
                self.records[s1, s2] = True
                return True
        
        self.records[s1, s2] = False
        return False