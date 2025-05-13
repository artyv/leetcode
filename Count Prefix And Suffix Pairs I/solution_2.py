class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            if len(s1) > len(s2):
                return False
            i = 0
            while i < len(s1):
                if s1[i] != s2[i] or s1[-1-i] != s2[-1-i]:
                    return False
                i += 1
            return True
        
        l = len(words)
        counter = 0
        for i in range(l-1):
            for j in range(i+1, l):
                if isPrefixAndSuffix(words[i], words[j]):
                    counter += 1
        
        return counter