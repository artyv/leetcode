class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        len_nums = len(nums)
        if len_nums < 2 or p == 0:
            return 0
        
        nums.sort()
        l, r = 0, nums[-1] - nums[0]

        while l < r:
            mid = (l + r) // 2
            cnt, i = 0, 0
            while i+1 < len_nums:
                if (nums[i+1] - nums[i]) <= mid:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    r = mid
                    break
            else:
                l = mid + 1
        
        return l 
