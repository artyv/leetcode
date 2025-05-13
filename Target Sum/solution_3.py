class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target:
            return 0
        elif s == target:
            return 2**nums.count(0)
        
        
        new_target = (s-target) // 2
        l, r = 1, new_target-1
        d = Counter(nums)
        counter = 2**d.get(0, 0) * d.get(new_target, 0)
        while l < r:
            if d.get(l, 0) == 0 or d.get(r, 0) == 0:
                counter += max(d.get(l, 0), d.get(r, 0))
            else:
                counter += d.get(l) * d.get(r)
            l += 1
            r -= 1
        return counter