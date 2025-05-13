class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        elem = deque(nums[:k])
        max_sum = 0 if len(elem) != len(set(elem)) else sum(elem)
        temp_sum = sum(elem)
        for i in range(1, len(nums)-k+1):
            temp_sum += nums[i+k-1] - nums[i-1]
            elem.popleft()
            elem.append(nums[i+k-1])
            if len(elem) == len(set(elem)):
                max_sum = max(max_sum, temp_sum)
        return max_sum