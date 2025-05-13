class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(list(nums))
        d = defaultdict()
        for x in sorted_list:
            max_subset = []
            for y in d:
                if x % y == 0 and len(d[y]) > len(max_subset):
                    max_subset = d[y]
            d[x] = max_subset + [x]

        
        return max(d.values(), key=len)