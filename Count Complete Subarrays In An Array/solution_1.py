class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        len_nums = len(nums)
        counter, l = 0, 0
        cur_dist = 0
        cur_d = dict()
        for r, x in enumerate(nums):
            if x in cur_d:
                cur_d[x] += 1
            else:
                cur_dist += 1
                cur_d[x] = 1
            
            while l <= r and cur_dist == distinct:
                counter += len_nums - r
                cur_d[nums[l]] -= 1
                if cur_d[nums[l]] == 0:
                    del cur_d[nums[l]]
                    cur_dist -= 1
                l += 1
        
        return counter
