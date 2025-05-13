class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        l = len(nums)
        lis_length = [1] * l
        lds_length = [1] * l

        for i in range(l):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)

        # Stores the length of longest decreasing subsequence that starts at i.
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)

        n_min = 10**10
        for i in range(l):
            if lis_length[i] > 1 and lds_length[i] > 1:
                n_min = min(n_min, l - lis_length[i] - lds_length[i] + 1)

        return n_min