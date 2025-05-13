class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_set = set()
        for x in arr1:
            while x:
                arr1_set.add(x)
                x //= 10
        
        longest_prefix = 0
        for y in arr2:
            while y:
                if y in arr1_set:
                    longest_prefix = max(longest_prefix, len(str(y)))
                    break
                y //= 10
        
        return longest_prefix