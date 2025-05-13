class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        accum_sum = {0:1}
        temp_sum = 0
        counter = 0
        for i,x in enumerate(nums):
            temp_sum += x
            mod = temp_sum % k
            if mod < 0:
                mod += k
            
            if mod in accum_sum:
                counter += accum_sum[mod]
                accum_sum[mod] += 1
            else:
                accum_sum[mod] = 1
        
        return counter