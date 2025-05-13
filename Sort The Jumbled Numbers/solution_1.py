class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def my_mapping(n):
            output = 0
            dec = 1
            while n > 0:
                d = n % 10
                output = dec * mapping[d] + output
                dec *= 10
                n //= 10
            return output

        return sorted(nums, key=my_mapping)