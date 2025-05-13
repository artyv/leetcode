class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, M = len(haystack), len(needle)
        if N < M:
            return -1
        
        max_prefix = self.max_prefix_list(haystack)
        i = 0; j = 0
        while i < N:
            if haystack[i] == needle[j]:
                i += 1; j += 1
                if j == M:
                    return i - M
            else:
                if j > 0:
                    j = max_prefix[j-1]
                else:
                    i += 1
                    if i == N:
                        return -1

    def max_prefix_list(self, s):
        l = len(s)
        max_prefix = [0] * l
        j = 0; i = 1

        while i < l:
            if s[j] == s[i]:
                max_prefix[i] = j+1
                i += 1; j += 1
            else:
                if j == 0:
                    max_prefix[i] = 0
                    i += 1
                else:
                    j = max_prefix[j-1]
        return max_prefix
