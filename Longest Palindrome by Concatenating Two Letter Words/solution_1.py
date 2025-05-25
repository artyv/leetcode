class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words)
        l_max = 0
        
        for word,count in d.items():
            word_rev = word[::-1]
            if word_rev == word:
                l_max += 4 * (count // 2)
                d[word] -= 2 * (count // 2)
            elif word_rev in d:
                min_count = min(d[word], d[word_rev])
                l_max += 4 * min_count
                d[word] -= min_count
                d[word_rev] -= min_count
        
        for word in d:
            if word == word[::-1] and d[word] > 0:
                l_max += 2
                break
        
        return l_max

