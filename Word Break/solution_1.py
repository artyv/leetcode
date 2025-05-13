class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
        subDict = [st for st in wordDict if st[0] == s[0]]
        for word in subDict:
            if s[:len(word)] == word:
                if self.wordBreak(s[len(word):], wordDict):
                    return True
                else:
                    continue
    
        return False