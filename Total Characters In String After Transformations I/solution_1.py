class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MODULO = 10**9 + 7
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                if i == 25:
                    new_freq[0] += freq[i]  # 'a'
                    new_freq[1] += freq[i]  # 'b'
                else:
                    new_freq[i + 1] += freq[i]
            freq = new_freq

        return sum(freq) % MODULO