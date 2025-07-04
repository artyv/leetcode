class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_ind = -1
        for i in range(len(s)):
            if s[i] != '9':
                max_ind = i
                break
        
        xmin = int(s.replace(s[0], '0'))
        xmax = int(s.replace(s[max_ind], '9'))

        return xmax - xmin
