class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        l = len(nums)
        aux = dict()
        for i in range(l-1):
            if nums[i] % 2 == nums[i+1] % 2:
                aux[i] = False
        
        res = []
        for x,y in queries:
            for i in range(x, y+1):
                if i in aux:
                    res.append(False)
                    break
            else:
                res.append(True)
        return res
        