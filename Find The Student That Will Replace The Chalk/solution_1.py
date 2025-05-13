class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        l = len(chalk)
        i = 0
        k %= sum(chalk)
        while True:
            if i == l:
                i %= l
            k -= chalk[i]
            if k < 0:
                return i
            i += 1