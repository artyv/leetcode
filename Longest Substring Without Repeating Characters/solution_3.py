class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0; lmax = 0
        for right in range(len(s)):
            if len(s[left:right+1]) == len(set(s[left:right+1])):
                lmax = max(lmax, right-left+1)
            else:
                left += 1
        return lmax