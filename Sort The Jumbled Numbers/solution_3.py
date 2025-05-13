class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def my_mapping(n):
            s = str(n)
            output = ''
            for c in s:
                output += str(mapping[int(c)])
            return int(output)

        return sorted(nums, key=my_mapping)