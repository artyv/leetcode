class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1; r = max(nums)

        def is_possible(max_balls_bag):
            total_operations = 0
            for x in nums:
                operations = math.ceil(x / max_balls_bag) - 1
                total_operations += operations

                if total_operations > maxOperations:
                    return False
            return True
        
        while l < r:
            mid = (l+r) // 2
            if is_possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l