class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = len(nums)
        left = 0; right = nums[-1] - nums[0]

        def count_pairs(max_distance):
            counter = 0
            j = 0

            for i in range(l):
                while j < l and nums[j] - nums[i] <= max_distance:
                    j += 1
                counter += (j-1) - i
            return counter

        while left < right:
            mid = (left+right) // 2
            if count_pairs(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left