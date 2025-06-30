class Solution:
    def findLHS(self, nums: List[int]) -> int:
        lmax = 0
        counter = Counter(nums)
        for k,v in counter.items():
            if (k+1) in counter:
                lmax = max(lmax, counter[k] + counter[k+1])
        return lmax
