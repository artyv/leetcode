class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs
        
        strs.sort()
        s = ''
        for i in range(len(strs[0])):
            if strs[0][:i+1] in strs[-1][:i+1]:
                s += strs[0][i]
        return s
