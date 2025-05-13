class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        accum_sum = defaultdict(int)
        accum_sum[0] = 1
        temp_sum = 0; counter = 0
        for x in nums:
            temp_sum += x
            
            if (temp_sum % k) in accum_sum:
                counter += accum_sum[temp_sum%k]
            accum_sum[temp_sum%k] += 1
        
        return counter