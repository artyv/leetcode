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

            i = 0; start = 0; lm = 0
            stemp = ''
            while i < len(s):
                if len(s[start:i+1]) == len(set(s[start:i+1])):
                    lm = max(lm, len(s[start:i+1]))
                    i += 1
                else:
                    start = i
            return lm