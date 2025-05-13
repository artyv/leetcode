class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        s_temp = sum(list(map(int, num)))
        if s_temp % 2 != 0:
            return 0
        target = s_temp // 2
        
        counter = Counter(map(int, num))
        n = len(num)
        MODULO = 10**9 + 7
        
        max_odd = (n + 1) // 2

        psum = [0] * 11
        for i in range(9, -1, -1):
            psum[i] = psum[i + 1] + counter[i]

        @lru_cache(None)
        def dfs(pos, curr_sum, odd_left):
            if odd_left < 0 or psum[pos] < odd_left or curr_sum > target:
                return 0
            if pos > 9:
                return int(curr_sum == target and odd_left == 0)

            even_left = psum[pos] - odd_left
            total_ways = 0

            for i in range(max(0, counter[pos] - even_left), min(counter[pos], odd_left) + 1):
                odd_ways = comb(odd_left, i)
                even_ways = comb(even_left, counter[pos] - i)
                ways = odd_ways * even_ways % MODULO
                total_ways += ways * dfs(pos + 1, curr_sum + i * pos, odd_left - i)
                total_ways %= MODULO

            return total_ways

        return dfs(0, 0, max_odd)