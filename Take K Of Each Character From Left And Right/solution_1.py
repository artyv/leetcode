class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        len_s = len(s)
        if len_s < 3 * k:
            return -1
        
        left = 0
        lmin = len_s + 1
        counter = Counter()
        s = 2*s

        for right in range(2*len_s):
            counter[s[right]] += 1
            while counter['a'] >= k and counter['b'] >= k and counter['c'] >= k:
                lmin = min(lmin, right - left + 1)
                counter[s[left]] -= 1
                left += 1

        return -1 if lmin > len_s else lmin 