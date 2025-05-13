class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        aux = [x%2 for x in nums]
        prefix_count = [0] * (len(nums)+1)
        prefix_count[0] = 1
        
        counter = 0; prefix_sum = 0
        for x in aux:
            prefix_sum += x
            if prefix_sum >= k:
                counter += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1
        return counter