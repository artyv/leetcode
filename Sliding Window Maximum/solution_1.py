class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        nmax = max(nums[:k])
        a = [nmax]
        
        for i in range(1, len(nums)-k + 1):
            nmax = max(nums[i:i+k]) if nums[i-1] == nmax else max(nmax, nums[i+k-1])
            a += [nmax]
        
        return a
