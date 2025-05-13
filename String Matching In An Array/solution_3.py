class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        l = len(words)
        for i in range(l):
            for j in range(l):
                if j != i and words[i] in words[j]:
                    res.add(words[i])
        return list(res)