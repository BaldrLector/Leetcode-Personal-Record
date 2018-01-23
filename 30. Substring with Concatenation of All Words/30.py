class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def analyze(s, k, count):
            current_count = collections.Counter( [ s[i:i+k] for i in range(0,len(s)-k+1,k) ] )
            if current_count == count:
                return True
            return False
        
        if not words or not s:
            return []
        
        m = len(words)
        n = sum([len(word) for word in words])
        k = len(words[0])
        count = collections.Counter(words)
        
        if len(s) < n:
            return []
        
        result = []
        for begin in range(0, len(s) - n + 1):
            end = begin + n
            if analyze(s[begin:end], k, count):
                result += begin,
        return result