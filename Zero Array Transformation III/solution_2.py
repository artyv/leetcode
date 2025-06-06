class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        
        n = len(nums)
        m = len(queries)
        
        def check_possibility(k):
            heap = []
            delta = [0] * (n + 1)
            ops, j, used = 0, 0, 0

            for i in range(n):
                ops += delta[i]

                while j < m and queries[j][0] == i:
                    heappush(heap, -queries[j][1])
                    j += 1

                while ops < nums[i] and heap and -heap[0] >= i:
                    r = -heappop(heap)
                    ops += 1
                    if r + 1 <= n:
                        delta[r + 1] -= 1
                    used += 1

                if ops < nums[i]:
                    return False

            return used <= m - k

        left, right = 0, m

        kmax = -1
        while left <= right:
            mid = (right+left) // 2
            if check_possibility(mid):
                kmax = mid
                left = mid+1
            else:
                right = mid-1
        
        return kmax
