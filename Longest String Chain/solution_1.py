class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = {}

        for word in words:
            d[word] = 1
            for i in range(len(word)):
                stemp = word[:i] + word[i+1:]
                if stemp in d:
                    d[word] = max(d[word], 1 + d[stemp])
        return max(d.values())
                