class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        last_group = groups[0]

        for i in range(1, len(words)):
            if groups[i] != last_group:
                res.append(words[i])
                last_group = groups[i]
        
        return res
