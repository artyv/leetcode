class Solution:
    def maximumLength(self, s: str) -> int:
        substrings = []
        lc = s[0]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                lc += s[i+1]
            else:
                substrings.append(lc)
                lc = s[i+1]
        substrings.append(lc)

        print(substrings)
        substrings.sort()
        substrings.sort(key=len, reverse=True)
        print(substrings)

        l = -1
        for i in range(len(substrings)-2):
            if substrings[i] == substrings[i+1] and substrings[i] == substrings[i+2]:
                l = len(substrings[i])
        
        for sub in substrings:
            if len(sub) >= 3:
                l = max(l, len(sub)-2)
                break

        return l