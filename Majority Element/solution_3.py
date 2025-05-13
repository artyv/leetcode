class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {key:0 for key in set(nums)}

        for n in nums:
            cnt[n] += 1

        return max(cnt, key=cnt.get)