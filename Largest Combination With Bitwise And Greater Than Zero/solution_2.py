class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        lmax = 1; l = len(candidates)
        for i in range(l-1):
            if i > l - lmax:
                break
            x_total = candidates[i]
            lcur = 1
            for j in range(i+1, l):
                if x_total & candidates[j] != 0:
                    x_total &= candidates[j]
                    lcur += 1
                    lmax = max(lmax, lcur)
        return lmax