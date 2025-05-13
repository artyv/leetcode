class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target:
            return 0
        elif s == target:
            return 1 + nums.count(0)
        
        counter = 0
        new_target = (s-target) // 2
        l, r = 0, new_target
        d = Counter(nums)
        while l < r:
            if d.get(l, -1) == -1 or d.get(r, 0) == -1:
                counter += max(d.get(l, -1), d.get(r, -1))
            else:
                counter += d.get(l) * d.get(r)
            l += 1
            r -= 1
        return counter