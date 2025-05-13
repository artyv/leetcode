class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            if len(s1) > len(s2) or not(s2.startswith(s1)) or not(s2.endswith(s1)):
                return False
            return True
        
        l = len(words)
        counter = 0
        for i in range(l-1):
            for j in range(i+1, l):
                if isPrefixAndSuffix(words[i], words[j]):
                    counter += 1
        
        return counter