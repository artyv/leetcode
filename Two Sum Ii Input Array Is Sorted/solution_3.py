class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_len = len(numbers)
        for i, x in enumerate(numbers):
            needed = target - x
            left, right = i+1, num_len-1
            while left <= right:
                middle = (left+right) // 2
                if numbers[middle] == needed:
                    return [i+1, middle+1]
                elif numbers[middle] < needed:
                    left = middle + 1
                else:
                    right = middle - 1
            
        return [None, None]
