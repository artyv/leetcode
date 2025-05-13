class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        plus = []
        minus = []
        for n in nums:
            if n > 0:
                plus.append(n)
            else:
                minus.append(n)
        for i in range(l//2):
            nums[2*i] = plus[i]
            nums[2*i+1] = minus[i]
        return nums