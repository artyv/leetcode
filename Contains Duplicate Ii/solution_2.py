class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i, x in enumerate(nums):
            if x in d:
                if abs(d[x][-1] - i) <= k:
                    return True
                d[x].append(i)
            else:
                d[x] = [i]
        return False