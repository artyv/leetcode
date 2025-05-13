class Solution:
    def countDistinctPrimeFactors(self, num):
        distinct_primes = set()
        while num % 2 == 0:
            distinct_primes.add(2)
            num //= 2
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                distinct_primes.add(i)
                num //= i
        if num > 1:
            distinct_primes.add(num)
        return len(distinct_primes)

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        elements = [(i, self.countDistinctPrimeFactors(x), x) for i, x in enumerate(nums)]

        left_bound = [-1] * n
        right_bound = [n] * n

        stack = []
        for i, prime_score, value in elements:
            while stack and stack[-1][0] < prime_score:
                stack.pop()
            if stack:
                left_bound[i] = stack[-1][1]
            stack.append((prime_score, i))

        stack.clear()
        for i, prime_score, value in reversed(elements):
            while stack and stack[-1][0] <= prime_score:
                stack.pop()
            if stack:
                right_bound[i] = stack[-1][1]
            stack.append((prime_score, i))

        elements.sort(key=lambda x: -x[2])

        max_score = 1
        for i, prime_score, value in elements:
            left, right = left_bound[i], right_bound[i]
            contribution_count = (i - left) * (right - i)

            if contribution_count <= k:
                max_score = (max_score * pow(value, contribution_count, MOD)) % MOD
                k -= contribution_count
            else:
                max_score = (max_score * pow(value, k, MOD)) % MOD
                break

        return max_score