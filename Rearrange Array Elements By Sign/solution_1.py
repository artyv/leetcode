class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = [0] * l
        plus = 0; minus = 1
        for n in nums:
            if n > 0:
                output[plus] = n
                plus += 2
            else:
                output[minus] = n
                minus += 2
        return output