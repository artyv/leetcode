class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        aux = sorted([(x, i) for i,x in enumerate(nums)])
        n = len(nums)

        for i in range(n-k + 1):
            visited = set()
            visited.add(aux[i][1])
            for j in range(i+1, n):
                x, index = aux[j]
                if all(abs(i-index) >= 2 for i in visited):
                    visited.add(index)
                    if len(visited) == k:
                        return x
