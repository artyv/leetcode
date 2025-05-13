class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = [0] * k
        for x in arr:
            remainder[x % k] += 1
        l = 1; r = k-1
        while l < r:
            if remainder[l] != remainder[r]:
                return False
            l += 1; r -= 1
        if k % 2 == 0 and remainder[k%2] % 2 != 0:
            return False
        return True