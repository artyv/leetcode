class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n == 1:
                return False
            for x in range(2, int(sqrt(n))+1):
                if n % x == 0:
                    return False
            return True
        
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                continue
            for x in range(2, nums[i-1]):
                if nums[i-1] - x < nums[i] and is_prime(x):
                    nums[i-1] -= x
                    break
            else:
                return False
        return True