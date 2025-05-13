class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words) * len(words[0])

        comb = set(''.join(x) for x in permutations(words))

        indices = []

        for i in range(0, len(s) - k + 1):
            if s[i:i+k] in comb:
                indices.append(i)
        return indices