class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        xor = 0
        my_map = [0] * 26
        my_map[ord("a") - ord("a")] = 1
        my_map[ord("e") - ord("a")] = 2
        my_map[ord("i") - ord("a")] = 4
        my_map[ord("o") - ord("a")] = 8
        my_map[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        lmax = 0
        for i in range(len(s)):
            xor ^= my_map[ord(s[i]) - ord("a")]
            if mp[xor] == -1 and xor != 0:
                mp[xor] = i
            lmax = max(lmax, i - mp[xor])
        return lmax