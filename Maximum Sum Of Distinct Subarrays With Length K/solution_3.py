class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        elem = Counter(nums[:k])
        max_sum = 0 if len(elem) != k else sum(elem)
        temp_sum = sum(nums[:k])
        for i in range(1, len(nums)-k+1):
            temp_sum += nums[i+k-1] - nums[i-1]
            elem[nums[i-1]] -= 1
            if elem[nums[i-1]] == 0:
                del elem[nums[i-1]]
            
            elem[nums[i+k-1]] += 1
            if len(elem) == k:
                max_sum = max(max_sum, temp_sum)
        return max_sum