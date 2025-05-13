class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            '''lm = 1 
            for i in range(len(s) - 1):
                stemp = s[i]
                for j in range(i+1, len(s)):
                    stemp += s[j]
                    if len(stemp) != len(set(stemp)):
                        break
                    lm = max(len(stemp), lm)
            return lm'''

            start = 0; end = 0 
            lm = 0
            a = set()

            for end in range(0, len(s)):
                if s[end] not in a:
                    a.add(s[end])
                    lm = max(lm, len(s[start:end+1]))
                else:
                    start = s.find(s[end], start) + 1
            return lm