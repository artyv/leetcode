class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        lmax = 0
        left = 0; right = 0
        ascii_sum = 0
        while right <= len(s) - 1:
            ascii_sum += abs(ord(s[right]) - ord(t[right]))
            if ascii_sum <= maxCost:
                lmax = max(lmax, right-left+1)
                right += 1
            else:
                ascii_sum -= abs(ord(s[left]) - ord(t[left]))
                left += 1
                if left > right:
                    right += 1
        return lmax