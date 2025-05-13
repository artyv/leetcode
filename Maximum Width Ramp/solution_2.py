class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        l = len(nums); max_ramp = 0
        aux = []

        # Fill the stack with indices in increasing order of their values
        for i in range(l):
            if not aux or nums[aux[-1]] > nums[i]:
                aux.append(i)

        # Traverse the array from the end to the start
        for j in range(l-1, -1, -1):
            while aux and nums[aux[-1]] <= nums[j]:
                max_ramp = max(max_ramp, j-aux[-1])
                # Pop the index since it's already processed
                aux.pop()

        return max_ramp