class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: defaultdict(int))
        counter = 0

        for i, x in enumerate(nums):
            g_i = gcd(i, k)

            for g_j in d[x]:
                if (g_i * g_j) % k == 0:
                    counter += d[x][g_j]
            
            d[x][g_i] += 1

        return counter