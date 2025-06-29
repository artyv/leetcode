class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count_zeros = s.count('0')
        total_length = count_zeros
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                if int(s[i:], 2) <= k:
                    total_length += 1
                else:
                    break
        return total_length
