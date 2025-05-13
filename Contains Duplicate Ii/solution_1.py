class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i, x in enumerate(nums):
            if x in d:
                if abs(d[x] - i) <= k:
                    return True
            d[x] = i
        return False