class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        words_len = len(words)

        counter = Counter(words)
        indices = []

        for i in range(0, len(s) - k*words_len + 1):
            if s[i:i+k] in counter:
                    s_words = [s[i+k*j:i+k*(j+1)] for j in range(len(words))]
                    if Counter(s_words) == counter:
                        indices.append(i)
        return indices