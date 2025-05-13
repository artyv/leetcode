class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        l = len(chalk)
        i = 0
        while True:
            if i == l:
                i %= l
            k -= chalk[i]
            if k < 0:
                return i
            i += 1