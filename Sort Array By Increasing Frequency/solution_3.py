class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        def helper(a, b):
            if counter[a] > counter[b]:
                return 1
            elif counter[a] < counter[b]:
                return -1
            else:
                if a > b:
                    return -1
                else:
                    return 1
        return sorted(nums, key=cmp_to_key(helper))
        


