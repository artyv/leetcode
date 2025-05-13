class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        len_nums = len(nums)
        for i in range(len_nums):
            nums[i] = (nums[i] % modulo) == k
        
        prefix = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        res = 0

        for x in nums:
            prefix += x
            target_mod = (prefix - k) % modulo
            res += cnt[target_mod]
            cnt[prefix % modulo] += 1
        
        return res


        


