class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n_bags = len(nums) + maxOperations
        min_balls = math.ceil(sum(nums)/n_bags)

        def is_possible(max_balls_bag):
            total_operations = 0
            for x in nums:
                operations = math.ceil(x / max_balls_bag) - 1
                total_operations += operations

                if total_operations > maxOperations:
                    return False
            return True
        
        while not is_possible(min_balls):
            min_balls += 1
        
        return min_balls