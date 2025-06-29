class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(sorted(nums)[-k:])
        res = []
        for x in nums:
            if x in counter:
                counter[x] -= 1
                res.append(x)
                if counter[x] == 0:
                    del counter[x]
        return res
