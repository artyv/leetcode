class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = {}
        counter = 0

        for i, x in enumerate(nums):
            if x in d:
                for j in d[x]:
                    if i * j % k == 0:
                        counter += 1
                d[x].append(i)
            else:
                d[x] = [i]
        return counter