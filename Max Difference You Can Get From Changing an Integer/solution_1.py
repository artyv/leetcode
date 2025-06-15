class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        min_ind = max_ind = -1
        for i in range(len(s)):
            if max_ind == -1 and s[i] != '9':
                max_ind = i
                break
        
        xmax = int(s.replace(s[max_ind], '9'))

        for i in range(len(s)):
            if min_ind == -1 and s[i] > '1':
                min_ind = i
                break

        d_repl = '0' if s[0] == '1' else '1'
        xmin = int(s.replace(s[min_ind], d_repl)) if min_ind != -1 else num

        return xmax - xmin
