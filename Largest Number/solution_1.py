class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = list(map(str, nums))
        def comparator(a, b):
            return -1 if a + b > b + a else 1
        
        res.sort(key=cmp_to_key(comparator))
        if res[0] == '0':
            return '0'
        return ''.join(res)