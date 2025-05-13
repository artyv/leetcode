class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        l = len(nums)
        aux = []
        start = 0
        for i in range(1, l):
            if nums[i] % 2 == nums[i-1] % 2:
                aux.append((start, i-1))
                start = i
        aux.append((start, l-1))
        
        res = []
        for x,y in queries:
            for a,b in aux:
                r = range(a, b+1)
                if x in r and y in r:
                    res.append(True)
                    break
            else:
                res.append(False)
        return res
        