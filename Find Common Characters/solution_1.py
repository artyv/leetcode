class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for c in set(words[0]):
            for times in range(words[0].count(c), 0, -1):
                if all(x.count(c) >= times for x in words):
                    for _ in range(times):
                        res.append(c)
                    break
        return res