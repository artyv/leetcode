class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, r = 0, 1
        lmax = 1
        xmin = xmax = nums[0]
        while r < len(nums):
            xmin = min(xmin, nums[r])
            xmax = max(xmax, nums[r])
            print(f"{l=} {r=}  {xmax=} {xmin=}")
            if xmax - xmin <= limit:
                lmax = max(lmax, r - l + 1)
            else:
                while nums[l] == nums[l+1]:
                    l += 1
                while l <= r:
                    l += 1
                    xmax = max(nums[l:r+1])
                    xmin = min(nums[l:r+1])
                    if xmax - xmin <= limit:
                        break
            r += 1
        return lmax